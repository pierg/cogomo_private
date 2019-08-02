from z3 import *


def sat_check(propositions):
    """Check the satisfiability of the keys of the dictionary passed
    If satisfiabile it returns True and an assignment example
    If insatisfiabile it returns False and the list of elements generating the insatisfiability (unsat_core)"""

    s = Solver()

    for name, value in propositions.items():
        for elem in value:
            s.assert_and_track(elem, name + ": " + str(elem))

    satis = s.check()
    if str(satis) == "sat":
        return True, s.model()
    else:
        return False, s.unsat_core()


def is_refinement(contract_1, contract_2):
    """
    Check if A1 >= A2 and if G1 <= G2
    """
    a_check = is_contained_in(contract_2.get_assumptions(), contract_1.get_assumptions())
    g_check = is_contained_in(contract_1.get_guarantees(), contract_2.get_guarantees())

    return a_check and g_check



def is_g_abstraction(contract_1_g, contract_2_g):
    """
    Check contract_1_g is an abstraction of contract_2_g
    """
    g_check = is_contained_in(contract_1_g, contract_2_g)

    return g_check


def greedy_selection(top_level_contract, candidate_compositions):
    """
    Scan all the possible compositions and compute entropy and information gain for each of them,
    returns the element with more information gain
    :param top_level_contract:
    :param candidate_compositions: list of list of contracts
    :return: list of contracts
    """
    best_candidate = None
    best_gain = 0
    entropy_top = top_level_contract.compute_entropy()
    n_guarantee_assumtions_top = len(top_level_contract.get_assumptions()) + len(top_level_contract.get_guarantees())
    for candidate in candidate_compositions:
        candidate_gain = (
            entropy_top - (len(elem.get_guarantees()) / n_guarantee_assumtions_top) * elem.compute_entropy()
            for elem in candidate)
        if candidate_gain >= best_gain:
            best_candidate = candidate
    return best_candidate


def is_contained_in(prop_1, prop_2):
    """
    Checks if prop_1 is contained in prop_2, i.e. prop_2 is a bigger set
    :param prop_1: single proposition or list of propositions
    :param prop_2: single proposition or list of propositions
    :return:

    Example:
    print("~~~~~ Refinement Check ~~~~~~"
    x, y, z = Ints('x y z')

    s1 = Function('S1', IntSort(), BoolSort())
    s2 = Function('S2', IntSort(), BoolSort())

    s.assert_and_track(ForAll(x, If(And(x < 5, x > 3), s1(x) == True, s1(x) == False)), "x < 5, x > 3")
    s.assert_and_track(ForAll(y, If(And(y < 4, y > -2), s2(y) == True, s2(y) == False)), "y < 4, y > -2")

    s.add(ForAll(y, Implies(s2(y), s1(y))))

    print s.check()
    print s.unsat_core()
    """
    # TODO: proper refinement check
    # s = Solver()

    # convert to list
    if not isinstance(prop_1, list):
        prop_1 = [prop_1]

    if not isinstance(prop_2, list):
        prop_2 = [prop_2]

    if False in prop_2:
        return True

    # Checks if prop_1 contains at least all the elements of prop_2
    result = all(elem in prop_1 for elem in prop_2)

    return result


def consistency_check(goal):
    """Check Goal Consistency by satisfying the conjunction of all its guarantees
    If consistent it returns True and an assignment example
    If inconsistent it returns False and the list of elements generating the inconsistency (unsat_core)"""

    s = Solver()

    guarantees = goal.get_guarantees()

    for elem in guarantees:
        s.assert_and_track(elem, goal.get_name() + "_G: " + str(elem))

    satis = s.check()
    if str(satis) == "sat":
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

    satis = s.check()
    if str(satis) == "sat":
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

    satis = s.check()
    if str(satis) == "sat":
        return True, s.model()
    else:
        return False, s.unsat_core()
