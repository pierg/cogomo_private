from contracts.sat_checks import *

# Importing
import itertools as it

from collections import defaultdict


class NotSynthesizableError(Exception):
    """
    raised if it is not possible to synthesize
    """
    pass


# Each component is an A/G contract
class ContractLibrary:

    def __init__(self, name, contracts=None):

        if contracts is None:
            contracts = []
        self.name = name

        # Contracts is a list of Assumption/Guarantee pairs
        self.contracts = contracts

    def get_name(self):
        return self.name

    def get_contracts(self):
        return self.contracts

    def add_contracts(self, contracts):
        for contract in contracts:
            self.contracts.append(contract)

    def synthetise(self, spec_contract, minimize_components=True):
        """
        Looks among the component library a refinement of 'spec_contract'
        :param minimize_components:
        :param spec_contract: specification to be satisfied / refined
        :return: composition of the components that refine spec
        """

        # List of first level candidate refinements
        candidates = defaultdict(list)
        for guarantee in spec_contract.get_guarantees():
            for contract in self.contracts:
                # check guarantee refinement
                if is_contained_in(contract.get_guarantees(), guarantee):
                    if False not in spec_contract.get_assumptions():
                        # Check assumption compatibility
                        assumptions = {contract.get_name(): contract.get_assumptions(),
                                       spec_contract.get_name(): spec_contract.get_assumptions()}
                        satis, model = sat_check(assumptions)
                        if satis:
                            candidates[guarantee].append(contract)
                        else:
                            print("Not Synthetisable")
                            print("Fix the following assumptions:\n" + str(model))
                            raise NotSynthesizableError
                    else:
                        # Propagates all the assumptions from the library of components
                        candidates[guarantee].append(contract)

        if len(candidates) == 0:
            print("No component in the library is a refinement of the specification)")
            raise NotSynthesizableError

        # Greedely choose the best componenent composition that refines the specification

        refined_contract = spec_contract

        # Candidates composition that refines all the guarantees
        candidates_compositions = [[value for (key, value) in zip(candidates, values)]
                                   for values in it.product(*candidates.values())]

        # Eliminate duplicates
        for i, c in enumerate(candidates_compositions):
            c = list(set(c))
            candidates_compositions[i] = c

        # Choose the "best" candidate
        candidate_composition = greedy_selection(refined_contract, candidates_compositions)

        print(candidate_composition)

        # Iteretevely check in the library if assumptions are provided by other contracts and compose
        # Candidate components for each assumption
        candidates = defaultdict(list)
        for assumption in candidate_composition.get_assumptions():
            for contract in self.contracts:
                if is_contained_in(assumption, contract.get_guarantees()):
                    candidates[assumption].append(contract)

        candidates_compositions = [[value for (key, value) in zip(candidates, values)]
                                   for values in it.product(*candidates.values())]

        # Eliminate duplicates
        for i, c in enumerate(candidates_compositions):
            c = list(set(c))
            candidates_compositions[i] = c

        # Choose the "best" candidate
        candidate_composition = greedy_selection(refined_contract, candidates_compositions)
