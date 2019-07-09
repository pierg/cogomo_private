from goal_model import *
from contracts.contract_model import *

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
goal_1 = GoalModel("goal_1", Contract([a == True],
                                       [b == True]))

# Goal 2 shares the variable d with Goal_1 as assumption
goal_2 = GoalModel("goal_2", [Contract([c == True],
                                       [d == True])])

# Composing two contracts...

goal_12 = compose_goals([goal_1, goal_2])

print("\n\n")
print goal_12


# Goal 0 has a conflict with Goal 1
goal_0 = GoalModel("goal_0", [Contract([b == False],
                                       [d == True])])

# Composing two contracts with conflict
try:
    goal_120 = compose_goals([goal_1, goal_0], "goal_120")

except:
    "Conflict"

print("\n\n")

# Adding new goal (Goal 3 shares the variable d with Goal_2 as assumption)
goal_3 = GoalModel("goal_3", [Contract([d == True],
                                       [e == True])])

# Composing with simplification...
goal_123 = compose_goals([goal_12, goal_3], "goal_123")

print("\n\n")
print goal_123

# More goals

# Goal 4
goal_4 = GoalModel("goal_4", [Contract([f == True],
                                       [g == True])])

# Goal 5
goal_5 = GoalModel("goal_5", [Contract([h == True],
                                       [i == True])])

# Manual Conjunction
goal_4_5_manual = GoalModel("goal_4_5_m", [Contract([f == True],
                                                    [g == True]),
                                           Contract([h == True],
                                                       [i == True])
                                           ])

# Conjoin operator
goal_4_5 = conjoin_goals([goal_4, goal_5], "goal_4_5")

print("\n\n")
print goal_4_5


# Composing with the rest
goal_4123_5123 = compose_goals([goal_123, goal_4_5], "goal_4123_5123")


print("\n\n")
print goal_4123_5123


