from z3 import *

from goal import *





def sat_check(propositions):
    """Check the satisfiability of the keys of the dictionary passed
    If satisfiabile it returns True and an assignment example
    If insatisfiabile it returns False and the list of elements generating the insatisfiability (unsat_core)"""

    s = Solver()

    for name, value in propositions.items():
        for elem in value:
            s.assert_and_track(elem, name + ": " + str(elem))

    sat = s.check()
    if str(sat) == "sat":
        return True, s.model()
    else:
        return False, s.unsat_core()




def consistency_check(goal):
    """Check Goal Consistency by satisfying the conjunction of all its guarantees
    If consistent it returns True and an assignment example
    If inconsistent it returns False and the list of elements generating the inconsistency (unsat_core)"""

    s = Solver()

    guarantees = goal.get_guarantees()

    for elem in guarantees:
        s.assert_and_track(elem, goal.get_name() + "_G: " + str(elem))

    sat = s.check()
    if str(sat) == "sat":
        return True, s.model()
    else:
        return False, s.unsat_core()


def compatibility_check(goal):
    """Check Goal Compatibility by satisfying the conjunction of all its assumptions
    If compatible it returns True and an assignment example
    If incompatible it returns False and the list of elements generating the incompatibility (unsat_core)"""

    s = Solver()

    assumptions = goal.get_assumptions()

    for elem in assumptions:
        s.assert_and_track(elem, goal.get_name() + "_A: " + str(elem))

    sat = s.check()
    if str(sat) == "sat":
        return True, s.model()
    else:
        return False, s.unsat_core()


def satisfiability_check(goal):
    """Check Goal Satisfiability by satisfying the conjunction of all its assumptions and gurantees
    If satisfiable it returns True and an assignment example
    If insatisfiable it returns False and the list of elements generating the insatisfiability (unsat_core)"""

    s = Solver()

    assumptions = goal.get_assumptions()
    guarantees = goal.get_guarantees()

    for elem in assumptions:
        s.assert_and_track(elem, goal.get_name() + "_A: " + str(elem))

    for elem in guarantees:
        s.assert_and_track(elem, goal.get_name() + "_G: " + str(elem))

    sat = s.check()
    if str(sat) == "sat":
        return True, s.model()
    else:
        return False, s.unsat_core()


def goal_check(goal):
    """Check Consistency, Compatibility and Satisfiability of one goal"""

    sat, model = consistency_check(goal)
    if not sat:
        print




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

        return True, GoalContract(name, a_list_simplified, g_list_simplified), None

    else:
        return False, None, unsat_core


def conjoin(name, goal_contracts):

    cnjoinable, unsat_core = check_composition(goal_contracts)

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

        return True, GoalContract(name, a_list_simplified, g_list_simplified), None

    else:
        return False, None, unsat_core

