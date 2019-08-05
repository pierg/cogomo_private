from z3 import *
from contracts.sat_checks import *


x = z3.Real("x")

refined = And(x < 5, x > 3)

goal = x > 0

# sat = get_counterexamples(Implies(refined, goal))

sat = get_counterexamples([refined, goal])

sat = get_counterexamples(Implies(refined, goal))




# s = Solver()
#
#
# print "~~~~~ Refinement Check ~~~~~~"
# x, y, z = Ints('x y z')
#
# s1 = Function('S1', IntSort(), BoolSort())
# s2 = Function('S2', IntSort(), BoolSort())
#
# # s.add(Implies(p1, And(x < 5, x > -2)))
# # s.add(Implies(p2, And(y < 4)))
#
#
# s.assert_and_track(ForAll(x, If(And(x < 5, x > 3), s1(x) == True, s1(x) == False)), "x < 5")
# s.assert_and_track(ForAll(y, If(And(y < 4, y > -2), s2(y) == True, s2(y) == False)), "x < 4")
#
# s.add(ForAll(y, Implies(s2(y), s1(y))))
#
# print s.check()
# print s.unsat_core()