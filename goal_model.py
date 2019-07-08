from contracts.contract_operations import *
import itertools


class GoalModel:

    def __init__(self, name, contracts,
                 sub_goals=None,
                 sub_operation=None,
                 parent_goal=None,
                 parent_operation=None):

        if parent_goal is None:
            parent_goal = []
        if sub_goals is None:
            sub_goals = []
        self.name = name

        # Contracts is a list of Assumption/Guarantee pairs
        # Each element of the list is in conjunction with each other
        if not isinstance(contracts, list):
            self.contracts = [contracts]
        else:
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


class NotComposableError(Exception):
    """
    raised if it is not possible to compose
    """
    pass


class NotConjoinableError(Exception):
    """
    raised if it is not possible to conjoin
    """
    pass


def compose_goals(goals, name=None):
    """

    :param name: Name of the goal
    :param goals: List of goals to compose
    :return: composed_goals if success otherwise
    """

    contracts = {}

    for goal in goals:
        contracts[goal.get_name()] = goal.get_contracts()

    if name is None:
        name = '_'.join("{!s}".format(key) for (key, val) in contracts.items())

    composition_contracts = (dict(zip(contracts, x)) for x in itertools.product(*contracts.itervalues()))

    composed_contract_list = []
    for contracts in composition_contracts:
        satis, composed_contract = compose_contracts(contracts)
        if not satis:
            print("composition failed")
            raise NotComposableError
        composed_contract_list.append(composed_contract)

    # Creating a new Goal parent
    composed_goal = GoalModel(name, composed_contract_list,
                              sub_goals=goals,
                              sub_operation="COMPOSITION")

    # Connecting children to the parent
    for goal in goals:
        goal.set_parent(composed_goal, "COMPOSITION")

    return composed_goal


def conjoin_goals(goals, name):
    conjoined_contracts = []

    for goal in goals:
        conjoined_contracts.append(goal.get_contracts())

    # Flattening list
    conjoined_contracts = [item for sublist in conjoined_contracts for item in sublist]

    # TODO: fix checks on conjunction
    # sat = conjoin_contracts(conjoined_contracts)
    # if not sat:
    #     print("conjoin failed"
    #     return False, None

    # Creating a new Goal parent
    conjoined_goal = GoalModel(name, conjoined_contracts,
                               sub_goals=goals,
                               sub_operation="CONJUNCTION")

    # Connecting children to the parent
    for goal in goals:
        goal.set_parent(conjoined_goal, "CONJUNCTION")

    return conjoined_goal
