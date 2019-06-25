from sat_checks import *

# Each component is an A/G contract
class ComponentLibrary():

    def __init__(self, name, contracts=[]):

        self.name = name

        # Contracts is a list of Assumption/Guarantee pairs
        self.contracts = contracts

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.name)
        for contract in self.contracts:
            ret += "(A: " + str(contract.get_assumptions()) + ", G: " + str(contract.get_guarantees()) + ") "
        ret += "\n"
        if len(self.sub_goals) > 0:
            ret += "\t" * level + "\t" + self.sub_operation + "\n"
            level += 1
        for child in self.sub_goals:
            ret += child.__str__(level + 1)
        return ret


    def get_name(self):
        return self.name

    def get_contracts(self):
        return self.contracts

    def add_contracts(self, contract):
        self.contracts.append(contract)

    def synthetise(self, spec_contract):
        # TODO
        """
        Looks among the component library a refinement of 'spec'
        :param spec: specification to be satisfied / refined
        :return: composition of the components that refine spec
        """

        refined_contract = None
        for contract in self.contracts:
            if is_refinement(spec_contract, contract):
                if refined_contract is not None:
                    if is_better_refinement(contract, refined_contract):
                        refined_contract = contract
                else:
                    refined_contract = contract

        # Check library if assumptions are provided by other contracts and compose

        # Candidate components for each assumption
        candidate_components = {}
        for assumption in refined_contract.get_assumptions:
            for contract in self.contracts:
                if is_contained_in(assumption, contract.get_guarantees):
                    candidate_components[assumption] = contract





