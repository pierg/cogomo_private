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

# Goal 1
goal_1 = GoalContract("goal_1", [Contract([a == True],
                                          [b == True])])

# Goal 2 shares the variable d with Goal_1 as assumption
goal_2 = GoalContract("goal_2", [Contract([c == True],
                                          [d == True])])

# Composing two contracts...

sat, goal_12 = compose_goals("goal_12", [goal_1, goal_2])

if sat:
    print "\n\n"
    print goal_12


# Goal 0 has a conflict with Goal 1
goal_0 = GoalContract("goal_0", [Contract([b == False],
                                          [d == True])])

# Composing two contracts with conflict

sat, goal_120 = compose_goals("goal_120", [goal_1, goal_0])


print "\n\n"

# Adding new goal (Goal 3 shares the variable d with Goal_2 as assumption)
goal_3 = GoalContract("goal_3", [Contract([d == True],
                                          [e == True])])

# Composing with simplification...
sat, goal_123 = compose_goals("goal_123", [goal_12, goal_3])

if sat:
    print "\n\n"
    print goal_123

# More goals

# Goal 4
goal_4 = GoalContract("goal_4", [Contract([f == True],
                                          [g == True])])

# Goal 5
goal_5 = GoalContract("goal_5", [Contract([h == True],
                                          [i == True])])

# Manual Conjunction
goal_4_5_manual = GoalContract("goal_4_5_m", [Contract([f == True],
                                                       [g == True]),
                                              Contract([h == True],
                                                       [i == True])
                                              ])

# Conjoin operator
sat, goal_4_5 = conjoin_goals("goal_4_5", [goal_4, goal_5])

if sat:
    print "\n\n"
    print goal_4_5


# Composing with the rest
sat, goal_4123_5123 = compose_goals("goal_4123_5123", [goal_123, goal_4_5])


if sat:
    print "\n\n"
    print goal_4123_5123


