from z3 import *

import itertools
import sys


from goal_model import *
from contract_model import *
from sat_checks import *
from utility import *



def compose_contracts(contracts_dictionary):

    assumptions = {}
    guarantees = {}

    for source_goal, propositions in contracts_dictionary.items():
        assumptions[source_goal + "_assumptions"] = propositions.get_assumptions()
        guarantees[source_goal + "_guarantees"] = propositions.get_guarantees()

    a_composition = assumptions.values()

    # CHECK COMPATILITY
    sat, model = sat_check(assumptions)
    if not sat:
        print "The composition is uncompatible"
        print "Fix the following assumptions:\n" + str(model)
        return False, model


    # CHECK CONSISTENCY
    sat, model = sat_check(guarantees)
    if not sat:
        print "The composition is inconsistent"
        print "Fix the following guarantees:\n" + str(model)
        return False, model


    # CHECK SATISFIABILITY
    sat, model = sat_check(merge_two_dicts(assumptions, guarantees))
    if not sat:
        print "The composition is unsatisfiable"
        print "Fix the following conditions:\n" + str(model)
        return False, model


    print "The composition is compatible, consistent and satisfiable. Composing now..."

    a_composition = assumptions.values()
    g_composition = guarantees.values()

    # Flatting the lists
    a_composition = [item for sublist in a_composition for item in sublist]
    g_composition = [item for sublist in g_composition for item in sublist]

    a_composition_simplified = a_composition[:]
    g_composition_simplified = g_composition[:]


    print "Assumptions:\n\t\t" + str(a_composition_simplified)
    print "Guarantees:\n\n\t\t" + str(g_composition_simplified)


    # Compare each element in a_composition with each element in g_composition
    for a_elem in a_composition:
        for g_elem in g_composition:
            # For the moment we just compare identical elements, but if g_elem is bigger than a_element then -> remove them
            if g_elem == a_elem:
                print "Simplifying assumption " + str(a_elem)
                a_composition_simplified.remove(a_elem)
                g_composition_simplified.remove(g_elem)


    return True, Contract(a_composition_simplified, g_composition_simplified)



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
            return None
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



