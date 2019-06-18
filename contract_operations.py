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



def conjoin_contracts(contracts_dictionary):
    # TODO: to fix checks on conjunction
    assumptions = {}
    guarantees = {}

    for source_goal, propositions in contracts_dictionary.items():
        assumptions[source_goal + "_assumptions"] = propositions.get_assumptions()
        guarantees[source_goal + "_guarantees"] = propositions.get_guarantees()


    # CHECK SATISFIABILITY
    sat, model = sat_check(merge_two_dicts(assumptions, guarantees))
    if not sat:
        print "The composition is unsatisfiable"
        print "Fix the following conditions:\n" + str(model)
        return False, model


    # CHECK CONSISTENCY
    sat, model = sat_check(guarantees)
    if not sat:
        print "The composition is inconsistent"
        print "Fix the following guarantees:\n" + str(model)
        return False, model


    print "The conjunction satisfiable."

    return True




