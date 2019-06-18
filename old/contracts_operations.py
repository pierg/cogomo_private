from z3 import *

from goal import *
from checks import *
from utility import *




def compose(name, goal_contracts):

    assumptions = {}
    guarantees = {}

    for goal in goal_contracts:
        assumptions[goal.get_name() + "_assumptions"] = goal.get_assumptions()
        guarantees[goal.get_name() + "_guarantees"] = goal.get_guarantees()


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

    a_composition = []
    g_composition = []

    for goal in goal_contracts:
        a_composition.append(goal.get_assumptions())
        g_composition.append(goal.get_guarantees())

    a_composition_simplified = a_composition[:]
    g_composition_simplified = g_composition[:]


    print "Assumptions:\n\t\t" + str(a_composition_simplified)
    print "Guarantees:\n\n\t\t" + str(g_composition_simplified)


    print "Simplifying assumptions..."
    # Compare each element in a_composition with each element in g_composition
    for a_elem in a_composition:
        for g_elem in g_composition:
            # For the moment we just compare identical elements, but if g_elem is bigger than a_element then -> remove them
            if g_elem == a_elem:
                a_composition_simplified.remove(a_elem)
                g_composition_simplified.remove(g_elem)

    return True, GoalContract(name, a_composition_simplified, g_composition_simplified)
    
    

def conjoin(name, goal_contracts):

    a_conjunction = []
    g_conjunction = []

    for goal in goal_contracts:
        a_conjunction.append(goal.get_assumptions())
        g_conjunction.append(goal.get_guarantees())



