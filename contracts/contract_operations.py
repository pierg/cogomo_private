from contract_model import *
from sat_checks import *
from utility import *


class WrongParametersError(Exception):
    """
    raised if the parameters passed are wrong
    """
    pass


def compose_contracts(contracts):
    """

    :param contracts: dictionary of goals or list of contracts to compose
    :return: True, contract which is the composition of the contracts in the goals or the contracts in the list
             False, unsat core of smt, list of proposition to fix that cause a conflict when composing
    """

    contracts_dictionary = {}
    # Transform list into a dictionary contract-name -> proposition
    if isinstance(contracts, list):
        for contract in contracts:
            contracts_dictionary[contract.get_name()] = contract
    elif isinstance(contracts, dict):
        contracts_dictionary = contracts
    else:
        raise WrongParametersError

    assumptions = {}
    guarantees = {}

    for name, contract in contracts_dictionary.items():
        assumptions[name + "_assumptions"] = contract.get_assumptions()
        guarantees[name + "_guarantees"] = contract.get_guarantees()

    # CHECK COMPATILITY
    satis, model = sat_check(assumptions)
    if not satis:
        print("The composition is uncompatible")
        print("Fix the following assumptions:\n" + str(model))
        return False, model

    # CHECK CONSISTENCY
    satis, model = sat_check(guarantees)
    if not satis:
        print("The composition is inconsistent")
        print("Fix the following guarantees:\n" + str(model))
        return False, model

    # CHECK SATISFIABILITY
    satis, model = sat_check(merge_two_dicts(assumptions, guarantees))
    if not satis:
        print("The composition is unsatisfiable")
        print("Fix the following conditions:\n" + str(model))
        return False, model

    print("The composition is compatible, consistent and satisfiable. Composing now...")

    a_composition = assumptions.values()
    g_composition = guarantees.values()

    # Flatting the lists
    a_composition = [item for sublist in a_composition for item in sublist]
    g_composition = [item for sublist in g_composition for item in sublist]

    # Eliminating duplicates of assertions
    a_composition = list(dict.fromkeys(a_composition))
    g_composition = list(dict.fromkeys(g_composition))

    a_composition_simplified = a_composition[:]
    g_composition_simplified = g_composition[:]

    print("Assumptions:\n\t\t" + str(a_composition_simplified))
    print("Guarantees:\n\n\t\t" + str(g_composition_simplified))

    # Compare each element in a_composition with each element in g_composition
    for a_elem in a_composition:
        for g_elem in g_composition:
            # For the moment we just compare identical elements,
            # it should be if g_elem is a bigger set than a_element then -> simplify it from the assumptions
            if g_elem == a_elem:
                print("Simplifying assumption " + str(a_elem))
                a_composition_simplified.remove(a_elem)
                # g_composition_simplified.remove(g_elem)

    return True, Contract(a_composition_simplified, g_composition_simplified)


def conjoin_contracts(contracts):

    contracts_dictionary = {}
    # Transform list into a dictionary contract-name -> proposition
    if isinstance(contracts, list):
        for contract in contracts:
            contracts_dictionary[contract.get_name()] = contract
    elif isinstance(contracts, dict):
        contracts_dictionary = contracts
    else:
        raise WrongParametersError

    assumptions = {}
    guarantees = {}

    for source_goal, propositions in contracts_dictionary.items():
        assumptions[source_goal + "_assumptions"] = propositions.get_assumptions()
        guarantees[source_goal + "_guarantees"] = propositions.get_guarantees()

    # CHECK CONSISTENCY
    satis, model = sat_check(guarantees)
    if not satis:
        print "The composition is inconsistent"
        print "Fix the following guarantees:\n" + str(model)
        return False

    print "The conjunction satisfiable."

    return True
