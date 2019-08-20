from goal_model import *
from contracts.contract_model import *
from case_study.case_study_variables import *
from z3 import *


p7 = velocity_lea > 0
p8 = distance_front > 0
p9 = velocity_ego_t > 0
p10 = velocity_ego_t1 > 0

assumptions = And(p7, p8, p9, p10)


increase_speed = Function('increase_speed', IntSort(), IntSort(), BoolSort())
decrease_speed = Function('decrease_speed', IntSort(), IntSort(), BoolSort())
maintain_speed = Function('maintain_speed', IntSort(), IntSort(), BoolSort())

velocity_ego_t, velocity_ego_t1 = Ints('velocity_ego_t velocity_ego_t1')


# assumptions = [
#     ForAll(velocity_ego_t,
#            Exists(velocity_ego_t1,
#                   If(velocity_ego_t1 > velocity_ego_t, increase_speed(velocity_ego_t, velocity_ego_t1) == True,
#                      increase_speed(velocity_ego_t, velocity_ego_t1) == False))),
#     ForAll(velocity_ego_t,
#         Exists(velocity_ego_t1,
#                     If(velocity_ego_t1 < velocity_ego_t, decrease_speed(velocity_ego_t, velocity_ego_t1) == True,
#                        decrease_speed(velocity_ego_t, velocity_ego_t1) == False)))
# ]

assertions = [
    If(velocity_ego_t1 > velocity_ego_t, increase_speed(velocity_ego_t, velocity_ego_t1) == True,
                     increase_speed(velocity_ego_t, velocity_ego_t1) == False),

    If(velocity_ego_t1 < velocity_ego_t, decrease_speed(velocity_ego_t, velocity_ego_t1) == True,
                     decrease_speed(velocity_ego_t, velocity_ego_t1) == False),

    If(velocity_ego_t1 == velocity_ego_t, maintain_speed(velocity_ego_t, velocity_ego_t1) == True,
                     maintain_speed(velocity_ego_t, velocity_ego_t1) == False),


    # Implies(decrease_speed(velocity_ego_t, velocity_ego_t1), velocity_ego_t1 < velocity_ego_t),
    # Implies(increase_speed(velocity_ego_t, velocity_ego_t1), velocity_ego_t1 > velocity_ego_t),
    # Implies(maintain_speed(velocity_ego_t, velocity_ego_t1), velocity_ego_t1 == velocity_ego_t),

    # velocity_ego_t1 > velocity_ego_t,
    # velocity_ego_t1 < velocity_ego_t

    # velocity_ego_t1 > velocity_ego_t,
    # velocity_ego_t1 < velocity_ego_t

    # Implies(distance_front > 0, velocity_ego_t1 > velocity_ego_t),
    # Implies(distance_front > 0, velocity_ego_t1 < velocity_ego_t)

    # increase_speed(velocity_ego_t, velocity_ego_t1),
    # decrease_speed(velocity_ego_t, velocity_ego_t1),
    #
    Implies(distance_front < D_platoon, increase_speed(velocity_ego_t, velocity_ego_t1) == True),
    Implies(distance_front == D_platoon, maintain_speed(velocity_ego_t, velocity_ego_t1) == True),
    Implies(distance_front > D_platoon, decrease_speed(velocity_ego_t, velocity_ego_t1) == True),
    #
    Implies(velocity_ego_t < velocity_lea, increase_speed(velocity_ego_t, velocity_ego_t1) == True),
    Implies(velocity_ego_t == velocity_lea, maintain_speed(velocity_ego_t, velocity_ego_t1) == True),
    Implies(velocity_ego_t > velocity_lea, decrease_speed(velocity_ego_t, velocity_ego_t1) == True),

    # If(distance_front > 0, increase_speed(velocity_ego_t, velocity_ego_t1) == True, increase_speed(velocity_ego_t, velocity_ego_t1) == False),
    # If(distance_front > 0, decrease_speed(velocity_ego_t, velocity_ego_t1) == True, decrease_speed(velocity_ego_t, velocity_ego_t1) == False)


    distance_front > 0

]


assertions2 = [
    velocity_ego_t1 > velocity_ego_t,
    velocity_ego_t == velocity_lea,
    velocity_ego_t1 == velocity_lea

]


assertionsUNSAT2 = [
    Implies(distance_front < D_platoon, velocity_ego_t1 > velocity_ego_t),
    Implies(distance_front > D_platoon, velocity_ego_t1 < velocity_ego_t),
    Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
    ForAll(distance_front, velocity_ego_t == velocity_lea),
    ForAll(distance_front, velocity_ego_t1 == velocity_lea)

]



assertionsUNSAT = [
    Implies(distance_front < D_platoon, velocity_ego_t1 > velocity_ego_t),
    Implies(distance_front > D_platoon, velocity_ego_t1 < velocity_ego_t),
    Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
    Implies(distance_front != D_platoon, velocity_ego_t == velocity_lea),
    Implies(distance_front != D_platoon, velocity_ego_t1 == velocity_lea)
]


assertions3_fix = [
    Implies(distance_front < D_platoon, velocity_ego_t1 > velocity_ego_t),
    Implies(distance_front >= D_platoon, velocity_ego_t1 < velocity_ego_t),
    Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
    Implies(distance_front == D_platoon, velocity_ego_t == velocity_lea),
    Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_lea)

]



assertions3 = [
    Implies(distance_front < D_platoon, velocity_ego_t1 > velocity_ego_t),
    Implies(distance_front >= D_platoon, velocity_ego_t1 < velocity_ego_t),
    Implies(distance_front == D_platoon, velocity_ego_t1 == velocity_ego_t),
    ForAll(distance_front,
        And(Implies(velocity_ego_t < velocity_lea, velocity_ego_t1 > velocity_ego_t),
        Implies(velocity_ego_t >= velocity_lea, velocity_ego_t1 < velocity_ego_t),
        Implies(velocity_ego_t == velocity_lea, velocity_ego_t1 == velocity_ego_t))
    )
    # velocity_ego_t == velocity_lea,
    # velocity_ego_t1 == velocity_lea

]


x, x1, y, z = Ints('x x1 y z')

assertions_test = [
    x > x1,
    x == z,
    x1 == z
]


assumptions = [
    distance_front > 0,

]



# TEST
sat, unsat_core = sat_check_simple(assertionsUNSAT2)
print("\n...\n")
if not sat:
    get_counterexamples(unsat_core)
else:
    get_counterexamples(assertionsUNSAT2)


# get_counterexamples(Implies(And(assumptions), And(assertions)))

# sat, unsat_core = sat_check_simple([Implies(And(assumptions), And(assertions))])
#
# get_counterexamples(Implies(And(assumptions), And(assertions)))


