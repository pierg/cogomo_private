from contracts.contract_operations import *
import itertools


class GoalModel:

    def __init__(self, name, contracts,
                 sub_goals=None,
                 sub_operation=None,
                 parent_goal=None,
                 parent_operation=None):

        if sub_goals is None:
            sub_goals = []
        self.name = name

        self.abstracted = False

        # Contracts is a list of Assumption/Guarantee pairs
        # Each element of the list is in conjunction with each other
        if not isinstance(contracts, list):
            self.contracts = [contracts]
        else:
            self.contracts = contracts

        self.abstracted_contracts = []

        # List of children and its relationship with them (COMPOSITION / CONJUNCTION)
        self.sub_goals = sub_goals
        self.sub_operation = sub_operation

        # Parent goal and its relation (COMPOSITION / CONJUNCTION)
        self.parent_goal = parent_goal
        self.parent_operation = parent_operation

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for n, contract in enumerate(self.contracts):
            if n > 0:
                ret += "\t" * level + "\t/\\ \n"
            ret += "\t" * level + "A:\t\t" + \
                   ', '.join(str(x) for x in contract.get_assumptions()).replace('\n', ' ').replace(' ', '') + "\n"
            ret += "\t" * level + "G:\t\t" + \
                   ', '.join(str(x) for x in contract.get_guarantees()).replace('\n', ' ').replace(' ', '') + "\n"
            if contract.is_abstracted():
                ret += "\t" * level + "G_abs:\t" + \
                       ', '.join(str(x) for x in contract.get_abstract_guarantees()).replace('\n', ' ').replace(' ', '') + "\n"

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

    def get_subgoals_ops(self):
        return self.sub_goals, self.sub_operation

    def get_contracts(self):
        return self.contracts


    def substitute_goal(self, existing_goal, new_goal):
        """
        Search in the tree subgoals for existing_goal and substitutes it with new_goal,
        after substituting it propagates the assumptions to the top of the tree and performs all the checks
        :param existing_goal:
        :param new_goal:
        :return:
        """
        if self == existing_goal:

            # Substitute the leaf node with the new contracts and sub_goals
            self.contracts = new_goal.get_contracts()
            self.sub_goals, self.sub_operation = new_goal.get_subgoals_ops()

            # Update the parent contracts by composing/conjoining with the siblings
            parent = self.parent_goal
            updated = parent.update_tree()

            return updated and True

        if len(self.sub_goals) > 0:
            for goal in self.sub_goals:
                goal.substitute_goal(existing_goal, new_goal)


    def update_tree(self):
        """
        Recursively update tree bottom-up from the node
        :return:
        """
        if self.sub_operation == "COMPOSITION":
            contracts = {}

            for goal in self.sub_goals:
                contracts[goal.get_name()] = goal.get_contracts()

            composition_contracts = (dict(list(zip(contracts, x))) for x in itertools.product(*iter(contracts.values())))

            composed_contract_list = []
            for contracts in composition_contracts:
                satis, composed_contract = compose_contracts(contracts)
                if not satis:
                    print("update failed")
                    return False
                composed_contract_list.append(composed_contract)

                self.contracts = composed_contract_list

        elif self.sub_operation == "CONJUNCTION":
            conjoined_contracts = []

            for goal in self.sub_goals:
                conjoined_contracts.append(goal.get_contracts())
            # Flattening list
            conjoined_contracts = [item for sublist in conjoined_contracts for item in sublist]

            sat = conjoin_contracts(conjoined_contracts)
            if not sat:
                print("conjoin failed")
                return False

            self.contracts = conjoined_contracts

        if self.parent_goal is not None:
            self.parent_goal.update_tree()

        return True




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


def synthesize_goal(contract_library, spec, name=""):
    """
    Synthesize a goal which is a composition of contracts from the contract library that refines spec
    It also adds each contract as a subgoal, to keep track of the composition
    :param name:
    :param spec: Contract
    :param contract_library:
    :return: GoalModel
    """
    contract_list = contract_library.synthesize(spec)
    goals_list = []
    for contract in contract_list:
        goals_list.append(GoalModel(contract.get_name(), contract))
    # Compose a new goal abstracting the top level goal to the guarantees provided by the designer
    satis, new_goal = compose_goals(goals_list, name, abstract_on_guarantees=spec.get_guarantees())
    if satis:
        return new_goal


def compose_goals(goals, name=None, abstract_on_guarantees=None):
    """

    :param name: Name of the goal
    :param goals: List of goals to compose
    :return: True, composed_goals if successful
    """

    contracts = {}
    abstracted_contracts = {}

    for goal in goals:
        contracts[goal.get_name()] = goal.get_contracts()

    if name is None:
        name = '_'.join("{!s}".format(key) for (key, val) in list(contracts.items()))

    composition_contracts = (dict(list(zip(contracts, x))) for x in itertools.product(*iter(contracts.values())))

    composed_contract_list = []
    for contracts in composition_contracts:
        satis, composed_contract = compose_contracts(contracts, abstract_on_guarantees=abstract_on_guarantees)
        if not satis:
            print("composition failed")
            return False, None
        composed_contract_list.append(composed_contract)

    # Creating a new Goal parent
    composed_goal = GoalModel(name, composed_contract_list,
                              sub_goals=goals,
                              sub_operation="COMPOSITION")

    # Connecting children to the parent
    for goal in goals:
        goal.set_parent(composed_goal, "COMPOSITION")

    return True, composed_goal


def conjoin_goals(goals, name):
    conjoined_contracts = []

    for goal in goals:
        conjoined_contracts.append(goal.get_contracts())
    # Flattening list
    conjoined_contracts = [item for sublist in conjoined_contracts for item in sublist]

    sat = conjoin_contracts(conjoined_contracts)
    if not sat:
        print("conjoin failed")
        return False

    # Creating a new Goal parent
    conjoined_goal = GoalModel(name, conjoined_contracts,
                               sub_goals=goals,
                               sub_operation="CONJUNCTION")

    # Connecting children to the parent
    for goal in goals:
        goal.set_parent(conjoined_goal, "CONJUNCTION")

    return conjoined_goal
