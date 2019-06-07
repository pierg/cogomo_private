from z3 import *
from contracts_operations import *



class Goal():

    def __init__(self, name, assumptions, guarantees):

        self.name = name

        self.assumptions = assumptions

        self.guarantees = guarantees


    def get_name(self):
        return self.name

    def add_assumption(self, assumption):
        return self.assumptions.append(assumption)

    def set_assumptions(self, assumptions):
        self.assumptions = assumptions
        print self.assumptions

    # def add_condition_to_gurantees(self, condition):
    #     if len(self.guarantees) > 1:
    #         guar = And(for elem in self.guarantees)
    #         self.guarantees = [Implies(condition, self.guarantees[0])]
    #     else:
    #         self.guarantees = [Implies(condition, self.guarantees[0])]
    #     print self.guarantees


    def set_guarantees(self, guarantees):
        self.guarantees = guarantees

    def get_assumptions(self):
        return self.assumptions

    def get_guarantees(self):
        return self.guarantees

    def pretty_print_goal(self):
        print "\nNAME:          " + str(self.name)
        print "\nASSUMPTIONS:   " + str(self.assumptions)
        print "\nGUARANTEES:    " + str(self.guarantees)