from goal_model import *
from contracts.contract_model import *
from case_study_variables import *



a_accelerate_distance = [distance_front > D_platoon]
g_accelerate_distance = velocity_ego_t1 > velocity_ego_t
goal_accelerate_distance = GoalModel("accelerate_distance",
                                     Contract(a_accelerate_distance, g_accelerate_distance,
                                              name = "accelerate_distance"))

a_decellerate_distance = [distance_front < D_platoon]
g_decellerate_distance = velocity_ego_t1 < velocity_ego_t
goal_decellerate_distance = GoalModel("decellerate_distance",
                                      Contract(a_decellerate_distance, g_decellerate_distance,
                                               name = "decellerate_distance"))

a_maintainspeed_distance = [distance_front == D_platoon]
g_maintainspeed_distance = velocity_ego_t1 == velocity_ego_t
goal_maintainspeed_distance = GoalModel("maintainspeed_distance",
                                        Contract(a_maintainspeed_distance, g_maintainspeed_distance,
                                                 name="maintainspeed_distance"))


goal_keep_short_distance = conjoin_goals([goal_accelerate_distance, goal_decellerate_distance, goal_maintainspeed_distance], "keep_short_distance")


print(goal_keep_short_distance)


a_accelerate_follow = [velocity_ego_t < velocity_lea]
g_accelerate_follow = velocity_ego_t1 > velocity_ego_t
goal_accelerate_follow = GoalModel("accelerate_follow", Contract(a_accelerate_follow, g_accelerate_follow))


a_decellerate_follow = [velocity_ego_t > velocity_lea]
g_decellerate_follow = velocity_ego_t1 < velocity_ego_t
goal_decellerate_follow = GoalModel("decellerate_follow", Contract(a_decellerate_follow, g_decellerate_follow))


a_maintainspeed_follow = [velocity_ego_t == velocity_lea]
g_maintainspeed_follow = velocity_ego_t1 == velocity_ego_t
goal_maintainspeed_follow = GoalModel("maintainspeed_follow", Contract(a_maintainspeed_follow, g_maintainspeed_follow))


goal_follow_leader = conjoin_goals([goal_accelerate_follow, goal_decellerate_follow, goal_maintainspeed_follow], "follow_leader")

print goal_follow_leader

goal_platooning = conjoin_goals([goal_keep_short_distance, goal_follow_leader], "platooning")


print("Fixing them..")


a_accelerate_distance = [distance_front != D_platoon, distance_front > D_platoon]
g_accelerate_distance = velocity_ego_t1 > velocity_ego_t
goal_accelerate_distance = GoalModel("accelerate_distance",
                                     Contract(a_accelerate_distance, g_accelerate_distance,
                                              name = "accelerate_distance"))

a_decellerate_distance = [distance_front != D_platoon, distance_front < D_platoon]
g_decellerate_distance = velocity_ego_t1 < velocity_ego_t
goal_decellerate_distance = GoalModel("decellerate_distance",
                                      Contract(a_decellerate_distance, g_decellerate_distance,
                                               name = "decellerate_distance"))


goal_keep_short_distance = conjoin_goals([goal_accelerate_distance, goal_decellerate_distance], "keep_short_distance")


print(goal_keep_short_distance)


a_accelerate_follow = [distance_front == D_platoon, velocity_ego_t < velocity_lea]
g_accelerate_follow = velocity_ego_t1 > velocity_ego_t
goal_accelerate_follow = GoalModel("accelerate_follow", Contract(a_accelerate_follow, g_accelerate_follow))


a_decellerate_follow = [distance_front == D_platoon, velocity_ego_t > velocity_lea]
g_decellerate_follow = velocity_ego_t1 < velocity_ego_t
goal_decellerate_follow = GoalModel("decellerate_follow", Contract(a_decellerate_follow, g_decellerate_follow))



a_maintainspeed_follow = [distance_front == D_platoon, velocity_ego_t == velocity_lea]
g_maintainspeed_follow = velocity_ego_t1 == velocity_ego_t
goal_maintainspeed_follow = GoalModel("maintainspeed_follow", Contract(a_maintainspeed_follow, g_maintainspeed_follow))


goal_follow_leader = conjoin_goals([goal_accelerate_follow, goal_decellerate_follow, goal_maintainspeed_follow], "follow_leader")

print goal_follow_leader

goal_following = conjoin_goals([goal_keep_short_distance, goal_follow_leader], "following")

print goal_following


# Measuing Distance
a_measure_distance = []             # The designer doesn't know the assumptions
g_measure_distance = [(distance_front > 0),
                      Implies(distance_front > distance_real, (distance_front - distance_real) < Delta_m),
                      Implies(distance_front <= distance_real, (distance_real - distance_front) <= Delta_m)]
goal_measure_distance = GoalModel("measure_distance", Contract(a_measure_distance, g_measure_distance))

# Communicate di the Leader
a_communicate_leader = [sig_network, sig_rssi > RSSI_net]
g_communicate_leader = [velocity_lea >= 0, steering_lea <= 1, steering_lea >= -1]
goal_communicate_leader = GoalModel("communicate_leader", Contract(a_communicate_leader, g_communicate_leader))



composable, goal_following_mode = compose_goals([goal_following, goal_measure_distance, goal_communicate_leader], "following_mode")

if composable:
    print("\n\n------------------------LEADING---------------------------------------")
    print goal_following_mode
    print("------------------------\LEADING---------------------------------------")





# LEADING
a_control_vehicle = [ang_gas >= 0, break_req >= 0]
g_control_vehicle = [Implies(ang_gas > 0, acc_ego > 0), Implies(break_req > 0, acc_ego < 0),
                     Implies(ang_gas == 0, acc_ego == 0), Implies(break_req == 0, acc_ego == 0)]
goal_control_vehicle = GoalModel("control_vehicle", Contract(a_control_vehicle, g_control_vehicle))


a_keep_safety_distance = [distance_front > 0]
g_keep_safety_distance = [ForAll(velocity_ego_t, distance_front >= D_safe)]
goal_keep_safety_distance = GoalModel("keep_safety_distance", Contract(a_keep_safety_distance, g_keep_safety_distance))


a_communicate_followers = [sig_network, sig_rssi > RSSI_net]
g_communicate_followers = [connected_platoon == True]
goal_communicate_followers = GoalModel("communicate_followers", Contract(a_communicate_followers, g_communicate_followers))


composable, leading_goal = compose_goals([goal_control_vehicle,
                                          goal_keep_safety_distance,
                                          goal_communicate_followers], "leading")

if composable:
    print("\n\n------------------------LEADING---------------------------------------")
    print leading_goal
    print("------------------------\LEADING---------------------------------------")


# Conjoining them together

platooning = conjoin_goals([goal_following_mode, leading_goal], "platooning")

print("\n\n------------------------PLATOONING---------------------------------------")
print platooning
print("------------------------\PLATOONING---------------------------------------")

synthesized_measure_distance = synthesize_goal(contract_library, Contract(a_measure_distance, g_measure_distance),
                                               "measure_distance_synth")

print("\n\nNew Goal Synthesized from the library:")
print synthesized_measure_distance

print("\n\nSubstituting exisitng goal with synthesized one from library")
platooning.substitute_goal(goal_measure_distance, synthesized_measure_distance)

print("\n\n------------------------PLATOONING SYNTH---------------------------------------")
print(platooning)
print("------------------------\PLATOONING SYNTH---------------------------------------")

print("")


