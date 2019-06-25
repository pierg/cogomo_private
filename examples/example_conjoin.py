from z3 import *
from goal_model import *
from goal_operations import *
from contract_model import *



a = Bool('a')
b = Bool('b')
c = Bool('c')
d = Bool('d')
e = Bool('e')

f = Bool('f')
g = Bool('g')

h = Bool('h')
i = Bool('i')

l = Bool('l')
m = Bool('m')

# Goal 1
goal_1 = GoalContract("goal_1", [Contract([a == True],
                                          [b == True])])

# Goal 4
goal_4 = GoalContract("goal_4", [Contract([f == True],
                                          [g == True])])

# Goal 5
goal_5 = GoalContract("goal_5", [Contract([h == True],
                                          [i == True])])

# Conjoin operator
sat, goal_4_5 = conjoin_goals("goal_4_5", [goal_4, goal_5])

if sat:
    print "\n\n"
    print goal_4_5


# Composing with the rest
sat, goal_41_51 = compose_goals("goal_4123_5123", [goal_1, goal_4_5])


if sat:
    print "\n\n"
    print goal_41_51



# Goal 6
goal_6 = GoalContract("goal_6", [Contract([l == True],
                                          [m == True])])


# Conjoin again
sat, goal_6_41_51 = conjoin_goals("goal_6_41_51", [goal_41_51, goal_6])


if sat:
    print "\n\n"
    print goal_6_41_51