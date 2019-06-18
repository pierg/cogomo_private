
class Contract():

    def __init__(self, assumptions, guarantees):

        self.assumptions = assumptions
        self.guarantees = guarantees


    def add_assumption(self, assumption):
        return self.assumptions.append(assumption)

    def set_assumptions(self, assumptions):
        self.assumptions = assumptions
        print self.assumptions

    def set_guarantees(self, guarantees):
        self.guarantees = guarantees

    def get_assumptions(self):
        return self.assumptions

    def get_guarantees(self):
        return self.guarantees

    def pretty_print_contract(self):
        print "\nASSUMPTIONS:   " + str(self.assumptions)
        print "\nGUARANTEES:    " + str(self.guarantees)
