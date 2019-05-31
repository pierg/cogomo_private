from z3 import *

from goal import *


def consistency_check(propositions):
    s = Solver()

    for name, value in propositions.items():
            for elem in value:
                s.assert_and_track(elem, name + ": " + str(elem))

    sat = s.check()
    if str(sat) == "sat":
        return sat, s
    else:
        return sat, s


def check_composition(goal_contracts):

    # Checking Guarantees for Consistency

    assumptions = {}
    guarantees = {}

    for goal in goal_contracts:
        assumptions[goal.get_name() + "_assumptions"] = goal.get_assumptions()
        guarantees[goal.get_name() + "_guarantees"] = goal.get_guarantees()

    sat, solver = consistency_check(guarantees)

    if str(sat) == "sat":
        print "\n\tGuarantees are consistent"
        print "Example assignments:\n"
        print solver.model()
    else:
        print "\n\tGuarantees are inconsistent!"
        print "\tCounterexample:"
        print solver.model
        print "\tFix the following assumptions:"
        print solver.unsat_core()
        return False, solver.unsat_core()

    # Checking Assumptions for Consistency

    sat, solver = consistency_check(assumptions)

    print "\n\tList of Assumptions: \n\n" + str(solver.assertions())

    if str(sat) == "sat":
        print "\n\tAssumptions are consistent"
        print "Example assignments:\n"
        print solver.model()
    else:
        print "\n\tAssumptions are inconsistent!"
        print "\tCounterexample:"
        print solver.model()
        print "\tFix the following guarantees:"
        print solver.unsat_core()
        return False, solver.unsat_core()
    
    return True, []
    

def compose(name, goal_contracts):

    composable, unsat_core = check_composition(goal_contracts)

    if composable:

        print "Simplifying the Assumptions.."

        a_list = []
        g_list = []

        for goal in goal_contracts:
            a_list.append(goal.get_assumptions())
            g_list.append(goal.get_guarantees())

        a_list_simplified = a_list[:]
        g_list_simplified = g_list[:]

        # Compare each element in a_list with each element in g_list
        for a_elem in a_list:
            for g_elem in g_list:
                # For the moment we just compare identical elements, but if g_elem is bigger than a_element then -> remove them
                if g_elem == a_elem:
                    a_list_simplified.remove(a_elem)
                    g_list_simplified.remove(g_elem)

        return True, Goal(name, a_list_simplified, g_list_simplified), None

    else:
        return False, None, unsat_core
