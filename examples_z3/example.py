# Copyright (c) Microsoft Corporation 2015, 2016

# The Z3 Python API requires libz3.dll/.so/.dylib in the 
# PATH/LD_LIBRARY_PATH/DYLD_LIBRARY_PATH
# environment variable and the PYTHONPATH environment variable
# needs to point to the `python' directory that contains `z3/z3.py'
# (which is at bin/python in our binary releases).

# If you obtained example.py as part of our binary release zip files,
# which you unzipped into a directory called `MYZ3', then follow these
# instructions to run the example:

# Running this example on Windows:
# set PATH=%PATH%;MYZ3\bin
# set PYTHONPATH=MYZ3\bin\python
# python example.py

# Running this example on Linux:
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:MYZ3/bin
# export PYTHONPATH=MYZ3/bin/python
# python example.py

# Running this example on macOS:
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:MYZ3/bin
# export PYTHONPATH=MYZ3/bin/python
# python example.py


from z3 import *

# from sympy import *

s = Solver()


# x = Real('x')
# y = Real('y')
# s = Solver()
# s.add(x + y > 4)
# s.add(x > 1)
# s.add(x < 2)
# s.add(y > 1)
# s.add(y < 3)
# print(s.check())
# print(s.model())


# x = Int('x')
# # y = Int('y')
# # n = x + y >= 3
# # print "num args: ", n.num_args()
# # print "children: ", n.children()
# # print "1st child:", n.arg(0)
# # print "2nd child:", n.arg(1)
# # print "operator: ", n.decl()
# # print "op name:  ", n.decl().name()


# s = Solver()

#
# print "\n\n\n--   Unsat Core Example  --"
# p1, p2, p3, p4, p5, p6 = Bools('p1 p2 p3 p4 p5 p6')
# x, y = Ints('x y')
# radar = Bool('radar')
# s.add(Implies(p1, x > 0))
# s.add(Implies(p2, y > x))
# s.add(Implies(p3, y < -1))
# s.add(Implies(p4, y < 1))
# s.add(Implies(p5, y > -10))
# s.add(Implies(p6, radar))
# print s.check(p1, p2, p3, p4, p5, p6)
# print s.unsat_core()
# print s.check(p1, p2, p3, p5, p6)
# print s.unsat_core()
# print s.check(p1, p2, p5, p6)
#
#
#





# v, s_gps, s_radar, s_network, a, c_ego, p, d_rad, c_front, d_front = Bool('v, s_gps, s_radar, s_network, a, c_ego, p, d_rad, c_front, d_front')
#
# # a_conj = And(v, s_gps, s_radar, s_network, a, c_ego, p, d_rad, c_front)
# # g_conj = And(a, c_ego, p, d_rad, c_front, d_front)
# #
# # a_comp = Or(a_conj, Not(g_conj))
# # g_comp = g_conj
#
# a_conj = v & s_gps & s_radar & s_network & a & c_ego & p & d_rad & d_front
# g_conj = a & c_ego & p & d_rad & c_front & d_front
# a_comp = a_conj | ~ g_conj

# print a_comp
# print simplify(a_comp)
# print simplify(Or(And(v, a, c_ego), Not(And(a, c_ego))))
# print simplify(Or(And(v, s_gps, s_radar, s_network, a, c_ego, p, d_rad, c_front), Not(And(a, c_ego, p, d_rad, c_front, d_front))))


# SIMPLIFICATION EXAMPLE BOOLEAN


p1, p2, p3, p4, p5, p6 = Bools('p1 p2 p3 p4 p5 p6')
x, y = Ints('x y')
radar = Bool('radar')
# s.add(Implies(p1, x > 0))
# s.add(Implies(p2, y > x))
# s.add(Implies(p3, y < -1))
# s.add(Implies(p4, y < 1))
# s.add(Implies(p5, y > -10))
# s.add(Implies(p6, radar))
# print s.check(p1, p2, p3, p4, p5, p6)
# print s.unsat_core()
# print s.check(p1, p2, p3, p5, p6)
# print s.unsat_core()
# print s.check(p1, p2, p5, p6)
#



s.assert_and_track(x > 0, 'a1')
s.assert_and_track(y > x, 'a2')
s.assert_and_track(y < -1, 'a3')
s.assert_and_track(y < 1, 'a4')
s.assert_and_track(y > -10, 'a5')
s.assert_and_track(radar, 'a6')
print s.check()
print s.unsat_core()


# a, b, c = symbols('a, b c')
# # exp = a & b | ~ (b & c)
# #
# # print to_cnf(exp, simplify=True)
#
#
# a = Bool('a')
# b = Bool('b')
# c = Bool('c')
#
# exp = a & b | ~b | ~c
# # exp = Or(And(a, b), Not(And(b, c)))
# # exp = Or(And(a, b), Not(b), Not(c))
#
# print to_cnf(exp, simplify=True)











#
#
#
#
#
# print "\n\n\n--   Measure Distance Car in Front  --"
# p1, p2, p3, p4, p5, p6 = Bools('p1 p2 p3 p4 p5 p6')
# x, y = Reals('x y')
# radar = Bool('radar')
# s.add(Implies(p1, x > 0))
# s.add(Implies(p2, y > x))
# s.add(Implies(p3, y < 100))
# s.add(Implies(p4, y < 1))
# s.add(Implies(p5, y > 10))
# s.add(Implies(p6, radar))
# print s.check(p1, p2, p3, p4, p5, p6)
# print s.unsat_core()
# print s.check(p1, p2, p3, p5, p6)
# print s.unsat_core()
# print s.check(p1, p2, p3, p5, p6)
#
#
#
#
#
# print "\n\n\n--   Measure Distance Car in Front  --"
# p1, p2, p3, p4, p5, p6 = Bools('p1 p2 p3 p4 p5 p6')
# x1, x2 = Ints('x1 x2')
# s1 = Function('S1', IntSort(), BoolSort())
# s2 = Function('S2', IntSort(), BoolSort())
# radar = Bool('radar')
# s.add(Implies(p1, x1 < 10))
# s.add(Implies(p2, x2 < 10))
# s.add(Implies(p3, ForAll([x1, x2], x1 < x2)))
# sat = s.check(p1, p2, p3)
# print sat
# print s.model()
# print s.unsat_core()
#
#
#
#
#
# s1 = Function('S1', IntSort(), BoolSort())
# s2 = Function('S2', IntSort(), BoolSort())
#
#

#
# print "~~~~~ Refinement Check ~~~~~~"
# p1, p2, p3, p4, p5, p6 = Bools('p1 p2 p3 p4 p5 p6')
# x, y, z = Ints('x y z')
#
# s1 = Function('S1', IntSort(), BoolSort())
# s2 = Function('S2', IntSort(), BoolSort())
#
# # s.add(Implies(p1, And(x < 5, x > -2)))
# # s.add(Implies(p2, And(y < 4, y > -6)))
#
# s.add(ForAll(x, If(And(x < 5), s1(x) == True, s1(x) == False)))
# s.add(ForAll(y, If(And(y < 4), s2(y) == True, s2(y) == False)))
#
# s.add(ForAll(y, Implies(s2(y), s1(y))))
#
# print s.check()
# print s.unsat_core()

# sol = Solver()
#
# max_n = 31
#
# # Note: One have to set a max limit on fib
# #
# # https://stackoverflow.com/questions/6915227/can-z3-check-the-satisfiability-of-formulas-that-contain-recursive-functions
# # Leonardo de Moura:
# # """
# # The models produced by Z3 assign an interpretation for each uninterpreted function symbol. The models can
# # be viewed as functional programs. The current version does not produce recursive definitions.
# # The first example [Fibonacci] is satisfiable, but Z3 fails to produce an interpretation for fib because
# # it does not support recursive definitions. We have plans to extend Z3 in this direction.
# # """
# fib = Function("fib", IntSort(), IntSort())
# x = Int("x")
# # sol.add(fib(0) == 1)
# # sol.add(fib(1) == 1)
# # sol.add(ForAll(x, Implies(And(x >= 2, x <= max_n), fib(x) == fib(x-1) + fib(x-2))))
# # Simpler:
# sol.add(ForAll(x, If(And(x >= 2, x <= max_n), fib(x) == fib(x-1) + fib(x-2), fib(x) == 1)))
#
# # sol.add(x == fib(2))
# y = Int("y")
# z = Int("z")
# sol.add(y>0, y <= max_n, z >0, z <= max_n)
#
# sol.add(10946 == fib(y))
# sol.add(2178309 == fib(z))
#
# print sol
# if sol.check()==sat:
#     mod = sol.model()
#     # print "x:", mod.eval(x)
#     print "z:", mod.eval(z), "y:", mod.eval(y)
#     sol.add(z != mod.eval(z),y != mod.eval(y))
#
#


# (assert (forall ((x Int)) (=> (S1 x) (S2 x))))

# f = Function('f', IntSort(), IntSort())
# g = Function('g', IntSort(), IntSort())
# a, b, c = Ints('a b c')
# x = Int('x')
#
# s = Solver()
# s.set(auto_config=False, mbqi=False)
#
# s.add( ForAll(x, f(g(x)) == x, patterns = [f(g(x))]),
#        g(a) == c,
#        g(b) == c,
#        a != b )
#
# # Display solver state using internal format
# print s.sexpr()
# print s.check()


#
# m = s.model()
#
#
# x = Int('x')
# y = Int('y')
# f = Function('f', IntSort(), IntSort())
# s = Solver()
# s.add(f(f(x)) == x, f(x) == y, x != y)
# print s.check()
# m = s.model()
# print "f(f(x)) =", m.evaluate(f(f(x)))
# print "f(x)    =", m.evaluate(f(x))


#
# f = Function('f', IntSort(), IntSort(), IntSort())
# x, y = Ints('x y')
# print ForAll([x, y], f(x, y) == 0)
#
# a, b = Ints('a b')
# solve(ForAll(x, f(x, x) == 0), f(a, b) == 1)



# a = Real('a')
# b = Real('b')
# c = Real('c')
# d = Real('d')
# e = Real('e')
# g = Real('g')
# f = Real('f')
# cost = Real('cost')
#
# opt = Optimize()
# opt.add(a + b - 350 == 0)
# opt.add(a - g == 0)
# opt.add(c - 400 == 0)
# opt.add(b - d * 0.45 == 0)
# opt.add(c - f - e - d == 0)
# opt.add(d <= 250)
# opt.add(e <= 250)
#
# opt.add(cost == If(f > 0, f * 50, f * 0.4) + e * 40 + d * 20 +
#   If(g > 0, g * 50, g * 0.54))
#
# h = opt.minimize(cost)
# print "\n +++ \n"
# print h
# print opt.check()
# print opt.lower(h)
# print opt.model()

# s.add(x > 0)
# s.add(y > x)
# s.add(y < 1)
# print s.check()
# print s.unsat_core()


# rok = Bool('Rok')
# rok = Bool('Rok')
# cok = Real('x')
# s = Solver()
# s.add(Or(x < 5, x > 10))
# s.add(Or(p, x**2 == 2))
# s.add(Not(p))
#
#
# for c in s.assertions():
#     print c
#
# print s.statistics()
#
# print s.check()
# print(s.model())


# solve(Or(x < 5, x > 10), Or(p, x**2 == 2), Not(p))