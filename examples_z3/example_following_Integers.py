from z3 import *


def check_composition(goal):
    s = Solver()

    # Checking Guarantees
    for name, value in goal.items():
        if "g_" in name:
            for elem in value:
                s.assert_and_track(elem, name + ": " + str(elem))

    print "\n\tList of Guarantees: \n\n" + str(s.assertions())
    sat = s.check()
    if str(sat) == "sat":
        print "\n\tGuarantees are consistent"
        print "Example assignments:\n"
        print s.model()
    else:
        print "\n\tGuarantees are inconsistent!"
        print "\tCounterexample:"
        print s.model()
        print "\tFix the following conditions:"
        print s.unsat_core()
        return False

    s = Solver()
    # Checking Assumptions for Consistency
    for name, value in goal.items():
        if "a_" in name:
            for elem in value:
                s.assert_and_track(elem, name + ": " + str(elem))

    print "\n\tList of Assumptions: \n\n" + str(s.assertions())
    sat = s.check()
    if str(sat) == "sat":
        print "\n\tAssumptions are consistent"
        print "Example assignments:\n"
        print s.model()
    else:
        print "\n\tAssumptions are inconsistent!"
        print "\tCounterexample:"
        print s.model()
        print "\tFix the following conditions:"
        print s.unsat_core()
        return False

    print "Simplifying the Assumptions.."

    a_list = []
    g_list = []
    for key, value in following_goal.items():
        if "a_" in key:
            for elem in value:
                a_list.append(elem)
        if "g_" in key:
            for elem in value:
                g_list.append(elem)

    a_list_simplified = a_list[:]
    g_list_simplified = g_list[:]

    # Compare each element in a_list with each element in g_list
    for a_elem in a_list:
        for g_elem in g_list:
            # For the moment we just compare identical elements, but if g_elem is bigger than a_element then -> remove them
            if g_elem == a_elem:
                a_list_simplified.remove(a_elem)
                g_list_simplified.remove(g_elem)


    print "\tAssumptions:"
    print str(a_list) + "\nU ! (" + str(g_list) + ")"

    print "\n\tSimplified to..."
    print str(a_list_simplified) + "\nU ! (" + str(g_list_simplified) + ")"


# Contants:
delta_m = 1     # meters
RSSI_net = 60   # dbm
epsilon_d = 1


# Variables
d_front = Real('d_front')
d_real = Real('d_real')
v_ego = Real('v_ego')
s_ego = Real('s_ego')
s_network = Bool('s_network')   # network ON
s_rssi = Real('s_rssi')
v_leader = Real('v_leader')
s_leader = Real('s_leader')
D_i = Int('D_i')
V_i = Int('V_i')


following_goal = {
    "a_1": [Bool('a_1') == False],
    "g_1": [(d_front > 0), Implies(d_front > d_real, (d_front - d_real) < delta_m), Implies(d_front <= d_real, (d_real - d_front) <= delta_m)],

    "a_2": [d_front > 0],
    "g_2": [D_i < 50, D_i > 5, V_i < 100, V_i > 20,  ForAll(D_i, ForAll(V_i, v_ego == V_i))],
    "g_2": [ForAll(V_i, v_ego == V_i)],

    "a_3": [s_network, s_rssi > RSSI_net],
    "g_3": [v_leader >= 0, s_leader <= 1, s_leader >= -1],

    "a_4": [v_leader >= 0, s_leader <= 1, s_leader >= -1],
    "g_4": [ForAll(v_leader, v_ego == v_leader), ForAll(s_leader, s_ego == s_leader)]
}


leading_goal = {}


sat = check_composition(following_goal)

if not sat:

    print "\tFixing the Guarantees..."

    D_platoon = 15      # meters

    following_goal["g_2"] = [Implies(And(d_front <= D_platoon + epsilon_d, d_front >= D_platoon - epsilon_d), v_ego == V_i)]

    following_goal["g_4"] = [Implies(And(d_front > D_platoon + epsilon_d, d_front < D_platoon - epsilon_d),
                                     ForAll(v_leader, v_ego == v_leader), ForAll(s_leader, s_ego == s_leader))]

    sat = check_composition(following_goal)




