from goal_model import *
from contracts.contract_operations import *
import itertools as it
from collections import defaultdict


class NotSynthesizableError(Exception):
    """
    raised if it is not possible to synthesize
    """
    pass


class ContractLibrary:

    def __init__(self, name, contracts=None):

        if contracts is None:
            contracts = []
        self.name = name

        # List of contracts in the library
        self.contracts = contracts

    def __str__(self):
        raise NotImplementedError

    def get_name(self):
        return self.name

    def get_contracts(self):
        return self.contracts

    def add_contracts(self, contracts):
        for contract in contracts:
            self.contracts.append(contract)

    def synthetise(self, spec_contract,
                   maximise_gain=True):
        """
        Looks among the contract library for a refinement of 'spec_contract'
        :param spec_contract: specification to be satisfied / refined
        :return: GoalModel which is the composition of the contracts that refine spec
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
                        # Propagates all the assumptions from the library of contracts
                        candidates[guarantee].append(contract)

        if len(candidates) == 0:
            print "No contract in the library is a refinement of the specification"
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

        # List of lists to track the library contracts that composed refine the spec
        list_refining_contracts = []
        refining_contract_composition = refined_contract

        # Iteretevely check in the library if assumptions are provided by other contracts and compose
        while (True):

            # Choose the "best" candidate
            selection_list_refining_contracts = greedy_selection(refining_contract_composition, candidates_compositions)

            # Save to the list
            list_refining_contracts.append(selection_list_refining_contracts)

            # Compose the candidates
            satis, refining_contract_composition = compose_contracts(selection_list_refining_contracts)

            # Extract the assumptions
            refining_assumptions = refining_contract_composition.get_assumptions()

            # Candidate contracts for each assumption
            candidates = defaultdict(list)
            for assumption in refining_assumptions:
                for contract in self.contracts:
                    if is_contained_in(assumption, contract.get_guarantees()):
                        candidates[assumption].append(contract)

            if len(candidates) == 0:
                break

            candidates_compositions = [[value for (key, value) in zip(candidates, values)]
                                       for values in it.product(*candidates.values())]

            # Eliminate duplicates
            for i, c in enumerate(candidates_compositions):
                c = list(set(c))
                candidates_compositions[i] = c

        # Flattening the list of lists of contracts
        flat_list_refining_contracts = [item for sublist in list_refining_contracts for item in sublist]

        print(str(len(flat_list_refining_contracts)) +
              " contracts found in the library that composed refine the specifications")

        print("")