from goal_model import *
from contracts.contract_model import *
from case_study.case_study_variables import *
from z3 import *


# Goals
# FOLLOWING

# sat_check_simple([Implies(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t),
#           Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
#           Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t)]
# )
#
# sat_check_simple([ForAll(velocity_lea, And(velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea))])


# sat_check_simple([If(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t, velocity_ego_t1 == velocity_ego_t), velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea])


# sat_check_simple([velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea, velocity_ego_t1 == 4, velocity_lea == 10])


# p1 = ForAll(distance_front, If(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t,
#                                                    If(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t,
#                                                       velocity_ego_t1 < velocity_ego_t)))

# p2 = If(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t,
#      If(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t,
#      velocity_ego_t1 < velocity_ego_t))

# p1 = Implies(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t)
# p2 = Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t)
# p3 = Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t)


p1 = Implies(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t)
p2 = Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t)

p3 =  Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t)
p33 = Implies(distance_front < D_platoon, velocity_ego_t1 > velocity_ego_t)


p4 = ForAll(distance_front, Implies(velocity_lea > velocity_ego_t, velocity_ego_t1 > velocity_ego_t))
p5 = ForAll(distance_front, Implies(velocity_lea == velocity_ego_t, velocity_ego_t1 == velocity_ego_t))
p6 = ForAll(distance_front, Implies(velocity_lea < velocity_ego_t, velocity_ego_t1 < velocity_ego_t))


p33 = velocity_ego_t1 > velocity_ego_t
p34 = velocity_ego_t1 == velocity_lea


p7 = velocity_lea > 0
p8 = distance_front > 0
p9 = velocity_ego_t > 0
p10 = velocity_ego_t1 > 0

assumptions = And(p7, p8, p9, p10)



increase_speed = Function('increase_speed', IntSort(), IntSort(), BoolSort())

x, y = Ints('x y')

# lhs = ForAll(x, Exists(y, If(y > x, increase_speed(x,y) == True, increase_speed(x,y) == False)))

lhs = ForAll([x, y], If(y > x, increase_speed(x, y) == True, increase_speed(x, y) == False))

inc_s = increase_speed(5, 4)
#
# l1 = ForAll(x, Exists(y, increase_speed(y, x)))
# l2 = ForAll(x, Exists(y, increase_speed(y, x)))
#
#
# If(y > x, increase_speed(x,y) == True, increase_speed(x,y) == False))
# lhs = ForAll([x, y], If(y > x, increase_speed(x,y) == True, increase_speed(x,y) == False))
#


assertions = [
    # ForAll([x, y], If(y > x, increase_speed(x, y) == True, increase_speed(x, y) == False)),
    If(y > x, increase_speed(x, y) == True, increase_speed(x, y) == False),
    increase_speed(x, y),
    x == y
]

sat, unsat_core = sat_check_simple(assertions)


b1 = ForAll(velocity_lea, velocity_ego_t1 == velocity_lea)
b2 = ForAll(velocity_ego_t, velocity_ego_t1 == velocity_ego_t)
t1 = Implies(distance_front > 100, ForAll(velocity_lea, velocity_ego_t1 == velocity_lea))
t2 = Implies(distance_front <= 100, ForAll(velocity_ego_t, velocity_ego_t1 == velocity_ego_t))

guarantees = [
    velocity_lea > 0,
    velocity_ego_t1 > 0,
    velocity_ego_t > 0,
    Implies(distance_front > 100, ForAll(velocity_lea, velocity_ego_t1 == velocity_lea)),
    Implies(distance_front <= 100, ForAll(velocity_ego_t, velocity_ego_t1 == velocity_ego_t))
]

# sat, unsat_core = sat_check_simple([Implies(assumptions, guarantees)])
# sat, unsat_core = sat_check_simple([lhs])
# get_counterexamples([assertions])



print "\n\n..\n\n"
# get_counterexamples([p11, p12])


# get_counterexamples(Implies(assumptions, guarantees))
#




# p3 = Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t)

# p4 = velocity_ego_t == velocity_lea
# p5 = velocity_ego_t1 == velocity_lea



# get_counterexamples([p1, p2, p3, p4, p5, p6])

# p4 = ForAll(distance_front, And(velocity_ego_t == velocity_lea, velocity_ego_t1 == velocity_lea))

# p2 = Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_lea)

# p4 = ForAll(distance_front, velocity_ego_t1 == velocity_lea)

# p2 = velocity_ego_t1 == velocity_lea

# p3 = ForAll(velocity_lea, velocity_ego_t == velocity_lea)
# p4 = velocity_ego_t == velocity_ego_t1
# p4 = ForAll(distance_front, velocity_ego_t1 == velocity_lea)

# p8 = velocity_ego_t > 5
# p9 = velocity_ego_t1 < 3

# get_counterexamples(p1)

# if not sat:
#     get_counterexamples(unsat_core)
#
# get_counterexamples([p4, p8, p9])
#
#
# # sat, unsat_core = sat_check_simple([p3])
#
#
# if not sat:
#     get_counterexamples(unsat_core)



#
# a_keep_short_distance = []
# g_keep_short_distance_1 = [Implies(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t),
#                            Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
#                            Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t),
#                            ForAll(velocity_lea, And(velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea))]
#
# g_keep_short_distance_21 = [ForAll(distance_front, If(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t,
#                                                    If(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t,
#                                                       velocity_ego_t1 < velocity_ego_t)))]
#
#
# g_keep_short_distance_2 = [ForAll(distance_front, And(Implies(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t),
#                            Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
#                            Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t)))]
#
# g_keep_short_distance_3 = [Implies(distance_front > D_platoon, velocity_ego_t1 > velocity_ego_t),
#                            Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
#                            Implies(distance_front < D_platoon, velocity_ego_t1 < velocity_ego_t),
#                            velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea]
#
# goal_keep_short_distance = GoalModel("keep_short_distance", Contract(a_keep_short_distance, g_keep_short_distance_1))
#
#
# # a_follow_leader = [velocity_lea >= 0]
# # g_follow_leader = [velocity_ego_t1 == velocity_lea, velocity_ego_t == velocity_lea]
# # goal_follow_leader = GoalModel("follow_leader", Contract(a_follow_leader, g_follow_leader))
# #
# #
# # composable, following_goal = compose_goals([goal_keep_short_distance,
# #                                             goal_follow_leader], "following")
# #
# # if composable:
# #     print following_goal