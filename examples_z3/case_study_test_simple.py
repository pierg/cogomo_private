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


assumptions = [
    ForAll(velocity_ego_t,
           Exists(velocity_ego_t1,
                  If(velocity_ego_t1 > velocity_ego_t, increase_speed(velocity_ego_t, velocity_ego_t1) == True,
                     increase_speed(velocity_ego_t, velocity_ego_t1) == False))),
    ForAll(velocity_ego_t,
        Exists(velocity_ego_t1,
                    If(velocity_ego_t1 < velocity_ego_t, decrease_speed(velocity_ego_t, velocity_ego_t1) == True,
                       decrease_speed(velocity_ego_t, velocity_ego_t1) == False)))
]

assertions = [
    ForAll(velocity_ego_t,
           ForAll(velocity_ego_t1,
                  If(velocity_ego_t1 > velocity_ego_t, increase_speed(velocity_ego_t, velocity_ego_t1) == True,
                     increase_speed(velocity_ego_t, velocity_ego_t1) == False))),

    ForAll(velocity_ego_t,
           Exists(velocity_ego_t1,
                  If(velocity_ego_t1 <= velocity_ego_t, decrease_speed(velocity_ego_t, velocity_ego_t1) == True,
                     increase_speed(velocity_ego_t, velocity_ego_t1) == False)))
    # ForAll(velocity_ego_t,
    #     Exists(velocity_ego_t1,
    #                 If(velocity_ego_t1 < velocity_ego_t, decrease_speed(velocity_ego_t, velocity_ego_t1) == True,
    #                    decrease_speed(velocity_ego_t, velocity_ego_t1) == False))),
    # If(velocity_ego_t1 == velocity_ego_t, maintain_speed(velocity_ego_t, velocity_ego_t1) == True,
    #    maintain_speed(velocity_ego_t, velocity_ego_t1) == False),

    # If(distance_front < D_platoon, increase_speed(velocity_ego_t, velocity_ego_t1),
    #                           decrease_speed(velocity_ego_t, velocity_ego_t1)),
    #
    # velocity_ego_t1  < velocity_ego_t

    # increase_speed(velocity_ego_t, velocity_ego_t1),
    # decrease_speed(velocity_ego_t, velocity_ego_t1)


    # ForAll(distance_front, decrease_speed(velocity_ego_t, velocity_ego_t1))

    # ForAll(distance_front, decrease_speed(velocity_ego_t, velocity_ego_t1))

    # ForAll(distance_front, If(distance_front < D_platoon, increase_speed(velocity_ego_t, velocity_ego_t1),
    #    If(distance_front > D_platoon, decrease_speed(velocity_ego_t, velocity_ego_t1),
    #       maintain_speed(velocity_ego_t, velocity_ego_t1))))

    # ForAll(distance_front, maintain_speed(velocity_ego_t, velocity_ego_t1))

]

sat, unsat_core = sat_check_simple(Not(And(assertions)))

# get_counterexamples(Implies(And(assumptions), And(assertions)))

# sat, unsat_core = sat_check_simple([Implies(And(assumptions), And(assertions))])
#
# get_counterexamples(Implies(And(assumptions), And(assertions)))


