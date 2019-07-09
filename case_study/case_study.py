from goal_model import *
from contracts.contract_model import *
from case_study_variables import *



# Goals
# FOLLOWING
a_measure_distance = [] # The designer doesn't know the assumptions
g_measure_distance = [(distance_front > 0),
                      Implies(distance_front > distance_real, (distance_front - distance_real) < Delta_m),
                      Implies(distance_front <= distance_real, (distance_real - distance_front) <= Delta_m)]
c_measure_distance = GoalModel("measure_distance", Contract(a_measure_distance, g_measure_distance))

a_keep_short_distance = [distance_front > 0]
g_keep_short_distance = [ForAll(distance_front, If(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t,
                                                   If(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t,
                                                      velocity_ego_t1 < velocity_ego_t)))]
c_keep_short_distance = GoalModel("keep_short_distance", Contract(a_keep_short_distance, g_keep_short_distance))

a_communicate_leader = [sig_network, sig_rssi > RSSI_net]
g_communicate_leader = [velocity_lea >= 0, steering_lea <= 1, steering_lea >= -1]
c_communicate_leader = GoalModel("communicate_leader", Contract(a_communicate_leader, g_communicate_leader))

a_follow_leader = [velocity_lea >= 0]
g_follow_leader = [velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea]
c_follow_leader = GoalModel("follow_leader", Contract(a_follow_leader, g_follow_leader))



composable, following_goal = compose_goals([c_measure_distance,
                                      c_keep_short_distance,
                                      c_communicate_leader,
                                      c_follow_leader], "following")

if composable:
    print following_goal

else:
    # Fixing the guarantees
    g_keep_short_distance = [Implies(
And(distance_front <= D_platoon + Epsilon_d, distance_front >= D_platoon - Epsilon_d),
        ForAll(distance_front, If(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t,
                                  If(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t, velocity_ego_t1 < velocity_ego_t))))]
    c_keep_short_distance = GoalModel("keep_short_distance", Contract(a_keep_short_distance, g_keep_short_distance))

    g_follow_leader = [Implies(
        Or(distance_front > D_platoon + Epsilon_d, distance_front < D_platoon - Epsilon_d),
        velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea)]
    c_follow_leader = GoalModel("follow_leader", Contract(a_follow_leader, g_follow_leader))

    composable, following_goal = compose_goals([c_measure_distance,
                                          c_keep_short_distance,
                                          c_communicate_leader,
                                          c_follow_leader], "following")

    if composable:
        print("\n\n------------------------FOLLOWING---------------------------------------")
        print following_goal
        print("------------------------\FOLLOWING---------------------------------------")



# Synthesis of "Measure Distance Goal"


# LEADING
a_control_vehicle = [ang_gas >= 0, break_req >= 0]
g_control_vehicle = [Implies(ang_gas > 0, acc_ego > 0), Implies(break_req > 0, acc_ego < 0),
                     Implies(ang_gas == 0, acc_ego == 0), Implies(break_req == 0, acc_ego == 0)]
c_control_vehicle = GoalModel("control_vehicle", Contract(a_control_vehicle, g_control_vehicle))


a_keep_safety_distance = [distance_front > 0]
g_keep_safety_distance = [ForAll(velocity_ego_t, distance_front >= D_safe)]
c_keep_safety_distance = GoalModel("keep_safety_distance", Contract(a_keep_safety_distance, g_keep_safety_distance))


a_communicate_followers = [sig_network, sig_rssi > RSSI_net]
g_communicate_followers = [connected_platoon == True]
c_communicate_followers = GoalModel("communicate_followers", Contract(a_communicate_followers, g_communicate_followers))


composable, leading_goal = compose_goals([c_control_vehicle,
                                          c_keep_safety_distance,
                                          c_communicate_followers], "leading")

if composable:
    print("\n\n------------------------LEADING---------------------------------------")
    print leading_goal
    print("------------------------\LEADING---------------------------------------")


# Conjoining them together

platooning = conjoin_goals([following_goal, leading_goal], "platooning")

print("\n\n------------------------PLATOONING---------------------------------------")
print platooning
print("------------------------\PLATOONING---------------------------------------")

synthesized_measure_distance = synthesize_goal(contract_library, Contract(a_measure_distance, g_measure_distance),
                                               "measure_distance_synth")

print("\n\nNew Goal Synthesized from the library:")
print synthesized_measure_distance

print("\n\nSubstituting exisitng goal with synthesized one from library")
platooning.substitute_goal(c_measure_distance, synthesized_measure_distance)

print("\n\n------------------------PLATOONING SYNTH---------------------------------------")
print(platooning)
print("------------------------\PLATOONING SYNTH---------------------------------------")

print("")


