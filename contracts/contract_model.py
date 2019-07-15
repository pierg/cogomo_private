from contracts.sat_checks import *


class VoidContractException(Exception):
    pass

class Contract:

    def __init__(self, assumptions, guarantees, name=""):
        if isinstance(assumptions, list):
            self.assumptions = assumptions
        else:
            self.assumptions = [assumptions]
        if isinstance(guarantees, list):
            self.guarantees = guarantees
        else:
            self.guarantees = [guarantees]

        self.name = name

        # CHECK IF G ARE COINTAINED IN A
        contracts_dictionary = {}
        for name, contract in contracts_dictionary.items():
            contracts_dictionary[name + "_assumptions"] = self.assumptions
            contracts_dictionary[name + "_guarantees"] = self.guarantees

        satis, model = sat_check(contracts_dictionary)
        if not satis:
            print "The contract is empty"
            print "Fix the following conditions:\n" + str(model)
            raise VoidContractException

    def __str__(self):
        print("\nASSUMPTIONS:   " + str(self.assumptions))
        print("\nGUARANTEES:    " + str(self.guarantees))

    def get_name(self):
        return self.name

    def add_assumption(self, assumption):
        new_assumptions = self.assumptions
        new_assumptions.append(assumption)

        sat, model = sat_check(new_assumptions)
        if not sat:
            print("The new assumptions are uncompatible")
            print("Fix the following assumptions:\n" + str(model))
            return False, model

        return True, self.assumptions

    def set_assumptions(self, assumptions):
        self.assumptions = assumptions
        print self.assumptions

    def set_guarantees(self, guarantees):
        self.guarantees = guarantees

    def get_assumptions(self):
        return self.assumptions

    def get_guarantees(self):
        return self.guarantees

    # Not really an entropy. It's the ratio between guarantees and assumptions
    def compute_entropy(self):
        lg = len(self.guarantees)
        la = len(self.assumptions)

        return lg / (la + lg)
