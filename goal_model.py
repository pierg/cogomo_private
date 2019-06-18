
class GoalContract():

    def __init__(self, name, contracts,
                 sub_goals=[],
                 sub_operation=None,
                 parent_goal=[],
                 parent_operation=None):

        self.name = name

        # Contracts is a list of Assumption/Guarantee pairs
        # Each element of the list is in conjunction with each other
        self.contracts = contracts

        # List of children and its relationship with them (COMPOSITION / CONJUNCTION)
        self.sub_goals = sub_goals
        self.sub_operation = sub_operation

        # Parent goal and its relation (COMPOSITION / CONJUNCTION)
        self.parent_goal = parent_goal
        self.parent_operation = parent_operation

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

    def set_parent(self, parent_goal, parent_operation):
        self.parent_goal = parent_goal
        self.parent_operation = parent_operation

    def get_name(self):
        return self.name

    def get_contracts(self):
        return self.contracts
