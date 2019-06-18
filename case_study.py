from z3 import *
from goal_model import *
from goal_operations import *
from contract_model import *


# Contants:
delta_m = 1     # meters
RSSI_net = 60   # dbm
epsilon_d = 1
D_platoon = 10   # platooning distance
D_safe = 20     # safety distance


# Variables
d_front = Real('d_front')        # measured distance
d_real = Real('d_real')

vel_ego_t = Real('vel_ego_t')      # current speed of the vehicle, at time t
vel_ego_t1 = Real('vel_ego_t1')     # speed of the ego vehicle at time t+1

ste_ego = Real('ste_ego')


s_network = Bool('s_network')   # network ON
s_rssi = Real('s_rssi')
v_leader = Real('v_leader')
s_leader = Real('s_leader')



ang_gas = Real('ang_gas')
break_req = Real('break_req')
acc_ego = Real('acc_ego')


# Goals
# FOLLOWING
a_measure_distance = [Bool('a_1') == False]
g_measure_distance = [(d_front > 0),
                      Implies(d_front > d_real, (d_front - d_real) < delta_m),
                      Implies(d_front <= d_real, (d_real - d_front) <= delta_m)]
c_measure_distance = GoalContract("measure_distance", a_measure_distance, g_measure_distance)

a_keep_short_distance = [d_front > 0]
g_keep_short_distance = [ForAll(d_front, If(d_front > D_platoon, vel_ego_t1 > vel_ego_t,
                            If(d_front == D_platoon, vel_ego_t1 == vel_ego_t, vel_ego_t1 < vel_ego_t)))]
c_keep_short_distance = GoalContract("keep_short_distance", a_keep_short_distance, g_keep_short_distance)

a_communicate_leader = [s_network, s_rssi > RSSI_net]
g_communicate_leader = [v_leader >= 0, s_leader <= 1, s_leader >= -1]
c_communicate_leader = GoalContract("communicate_leader", a_communicate_leader, g_communicate_leader)


a_follow_leader = [v_leader >= 0]
g_follow_leader = [vel_ego_t1 == v_leader, vel_ego_t == v_leader]
c_follow_leader = GoalContract("follow_leader", a_follow_leader, g_follow_leader)


# # LEADING
# a_control_vehicle = [ang_gas >= 0, break_req >= 0]
# g_control_vehicle = [Implies(ang_gas > 0, acc_ego > 0), Implies(break_req > 0, acc_ego < 0),
#                      Implies(ang_gas == 0, acc_ego == 0), Implies(break_req == 0, acc_ego == 0)]
# c_control_vehicle = Goal("control_vehicle", a_control_vehicle, g_control_vehicle)
#
#
# a_keep_safety_distance = [d_front > 0]
# g_keep_safety_distance = [D_i < 50, D_i > 5, V_i < 100, V_i > 20,  ForAll(D_i, ForAll(V_i, vel_ego == V_i))]
# c_keep_safety_distance = Goal("keep_safety_distance", a_keep_safety_distance, g_keep_safety_distance)
#
#
# a_synch_followers = [d_front > 0]
# g_synch_followers = [D_i < 50, D_i > 5, V_i < 100, V_i > 20,  ForAll(D_i, ForAll(V_i, vel_ego == V_i))]
# c_synch_followers = Goal("synch_followers", a_synch_followers, g_synch_followers)


composable, new_goal = compose("following", [c_measure_distance, c_keep_short_distance, c_communicate_leader, c_follow_leader])

#
if composable:

    new_goal.pretty_print()

else:

    c_keep_short_distance.set_guarantees([Implies(
        And(d_front <= D_platoon + epsilon_d, d_front >= D_platoon - epsilon_d),
                ForAll(d_front, If(d_front > D_platoon, vel_ego_t1 > vel_ego_t,
                           If(d_front == D_platoon, vel_ego_t1 == vel_ego_t, vel_ego_t1 < vel_ego_t))))])


    c_follow_leader.set_guarantees([Implies(
        Or(d_front > D_platoon + epsilon_d, d_front < D_platoon - epsilon_d),
                vel_ego_t1 == v_leader, vel_ego_t == v_leader)])

    composable, new_goal = compose("following", [c_measure_distance, c_keep_short_distance, c_communicate_leader, c_follow_leader])

    if composable:

        new_goal.pretty_print_contract()

