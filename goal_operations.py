from goal_model import *
from contract_operations import *
from sat_checks import *
import itertools


def compose_goals(name, goals):

    contracts = {}

    composition_contracts = {}

    for goal in goals:
        contracts[goal.get_name()] = goal.get_contracts()

    # Cartesian product of the assumptions of different goals
    if sys.version_info.major > 2:
        composition_contracts = (dict(zip(contracts, x)) for x in itertools.product(*contracts.values()))

    composition_contracts = (dict(itertools.izip(contracts, x)) for x in itertools.product(*contracts.itervalues()))

    composed_contract_list = []
    for contracts in composition_contracts:
        sat, composed_contract = compose_contracts(contracts)
        if not sat:
            print "composition failed"
            return False, None
        composed_contract_list.append(composed_contract)


    # Creating a new Goal parent
    composed_goal = GoalContract(name, composed_contract_list,
                                 sub_goals=goals,
                                 sub_operation="COMPOSITION")

    # Connecting children to the parent
    for goal in goals:
        goal.set_parent(composed_goal, "COMPOSITION")

    return True, composed_goal
    
    

def conjoin_goals(name, goals):

    conjoined_contracts = []

    for goal in goals:
        conjoined_contracts.append(goal.get_contracts())

    # Flattening list
    conjoined_contracts = [item for sublist in conjoined_contracts for item in sublist]

    # Creating a new Goal parent
    conjoined_goal = GoalContract(name, conjoined_contracts,
                                 sub_goals=goals,
                                 sub_operation="CONJUNCTION")

    # Connecting children to the parent
    for goal in goals:
        goal.set_parent(conjoined_goal, "CONJUNCTION")

    return True, conjoined_goal



