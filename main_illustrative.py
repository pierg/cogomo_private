from z3 import *
from contracts_operations import *


a = Bool('a')
b = Bool('b')
c = Bool('c')
d = Bool('d')
e = Bool('e')

f = Bool('f')
g = Bool('g')


# Goal 1
a_goal_1 = [a == False]
g_goal_1 = [b == True]
c_goal_1 = Goal("goal_1", [(a_goal_1, g_goal_1)])

# Goal 2
a_goal_2 = [c == False]
g_goal_2 = [d == True]
c_goal_2 = Goal("goal_2", [(a_goal_2, g_goal_2)])

# Goal 3
a_goal_3 = [d == True]
g_goal_3 = [e == True]
c_goal_3 = Goal("goal_3", [(a_goal_3, g_goal_3)])


# Goal 4
a_goal_4 = [f == True]
g_goal_4 = [g == True]
c_goal_4 = Goal("goal_4", [(a_goal_4, g_goal_4)])


# Composing...

sat, goal_123 = compose("goal_123", [c_goal_1, c_goal_2, c_goal_3])

if sat:
    goal_123.pretty_print_goal()


sat, goal_123_4 = conjoin("goal_123_4", [goal_123, c_goal_4])




