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



def is_refinement(contract_1, contract_2):
    """
    Check if A1 >= A2 and if G1 <= G2
    """
    a_check = is_contained_in(contract_2.get_assumptios(), contract_1.get_assumptions())
    g_check = is_contained_in(contract_1.get_guarantees(), contract_2.get_gurantees())

    return (a_check and g_check)


def is_better_refinement(contract_1, contract_2):
    #TODO: compare two refinements
    return False



def is_contained_in(prop_1, prop_2):
    """
    Checks if prop_1 is a refinement of prop_2
    :param prop_1:
    :param prop_2:
    :return:

    Example:
    print "~~~~~ Refinement Check ~~~~~~"
    x, y, z = Ints('x y z')

    s1 = Function('S1', IntSort(), BoolSort())
    s2 = Function('S2', IntSort(), BoolSort())

    s.assert_and_track(ForAll(x, If(And(x < 5, x > 3), s1(x) == True, s1(x) == False)), "x < 5, x > 3")
    s.assert_and_track(ForAll(y, If(And(y < 4, y > -2), s2(y) == True, s2(y) == False)), "y < 4, y > -2")

    s.add(ForAll(y, Implies(s2(y), s1(y))))

    print s.check()
    print s.unsat_core()
    """
    s = Solver()
    #TODO: refinement check

    if prop_1 == False:
        return True
    return prop_1 == prop_2



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

