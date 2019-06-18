from z3 import *





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

