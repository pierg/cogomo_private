from sat_checks import *

class Contract():

    def __init__(self, assumptions, guarantees, name=""):

        self.assumptions = assumptions
        self.guarantees = guarantees
        self.name = name


    def __str__(self):
        print "\nASSUMPTIONS:   " + str(self.assumptions)
        print "\nGUARANTEES:    " + str(self.guarantees)


    def add_assumption(self, assumption):
        new_assumptions = self.assumptions
        new_assumptions.append(assumption)

        sat, model = sat_check(new_assumptions)
        if not sat:
            print "The new assumptions are uncompatible"
            print "Fix the following assumptions:\n" + str(model)
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

