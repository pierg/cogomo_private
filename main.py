from z3 import *
from contracts_operations import *


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


# Goals

a_measure_distance = [Bool('a_1') == False]
g_measure_distance = [(d_front > 0), Implies(d_front > d_real, (d_front - d_real) < delta_m), Implies(d_front <= d_real, (d_real - d_front) <= delta_m)]
c_measure_distance = Goal("measure_distance", a_measure_distance, g_measure_distance)

a_keep_distance = [d_front > 0]
g_keep_distance = [D_i < 50, D_i > 5, V_i < 100, V_i > 20,  ForAll(D_i, ForAll(V_i, v_ego == V_i))]
c_keep_distance = Goal("keep_distance", a_keep_distance, g_keep_distance)

a_communicate_leader = [s_network, s_rssi > RSSI_net]
g_communicate_leader = [v_leader >= 0, s_leader <= 1, s_leader >= -1]
c_communicate_leader = Goal("communicate_leader", a_communicate_leader, g_communicate_leader)


a_follow_leader = [v_leader >= 0, s_leader <= 1, s_leader >= -1]
g_follow_leader = [ForAll(v_leader, v_ego == v_leader), ForAll(s_leader, s_ego == s_leader)]
c_follow_leader = Goal("follow_leader", a_follow_leader, g_follow_leader)


composable, new_goal, unsat_conditions = compose("following", [c_measure_distance, c_keep_distance, c_communicate_leader, c_follow_leader])


if composable:

    new_goal.pretty_print()

else:
    # Fixing...

    D_platoon = 15      # meters

    c_follow_leader.set_guarantees([Implies(And(d_front > D_platoon + epsilon_d, d_front < D_platoon - epsilon_d),
                                     ForAll(v_leader, v_ego == v_leader), ForAll(s_leader, s_ego == s_leader))])

    c_keep_distance.set_guarantees([Implies(And(d_front <= D_platoon + epsilon_d, d_front >= D_platoon - epsilon_d), v_ego == V_i)])

    composable, new_goal, unsat_conditions = compose("following", [c_measure_distance, c_keep_distance, c_communicate_leader, c_follow_leader])

    if composable:

        new_goal.pretty_print_goal()

