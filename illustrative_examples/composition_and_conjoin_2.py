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

l = Bool('l')
m = Bool('m')

# Goal 1
goal_1 = GoalModel("goal_1", [Contract([a == True],
                                       [b == True])])

# Goal 4
goal_4 = GoalModel("goal_4", [Contract([f == True],
                                       [g == True])])

# Goal 5
goal_5 = GoalModel("goal_5", [Contract([h == True],
                                       [i == True])])

# Conjoin operator
goal_4_5 = conjoin_goals([goal_4, goal_5], "goal_4_5")

print("\n\n")
print goal_4_5


# Composing with the rest
goal_41_51 = compose_goals([goal_1, goal_4_5], "goal_4123_5123")

print("\n\n")
print goal_41_51



# Goal 6
goal_6 = GoalModel("goal_6", [Contract([l == True],
                                       [m == True])])


# Conjoin again
goal_6_41_51 = conjoin_goals([goal_41_51, goal_6], "goal_6_41_51")

print("\n\n")
print goal_6_41_51