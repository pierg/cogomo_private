from contracts.contract_library import *
from goal_model import *

a1 = Bool('a1')
a2 = Bool('a2')
a3 = Bool('a3')

b = Bool('b')
b2 = Bool('b2')


c = Bool('c')
d = Bool('d')
e = Bool('e')
f = Bool('f')
g = Bool('g')
h = Bool('h')
i = Bool('i')
l = Bool('l')
m = Bool('m')
n = Bool('n')
o = Bool('o')



contract_library = ContractLibrary("cogomo")


# Components
comp_1 = Contract([a1 == True, a2 == True], [b == True], name="comp_1")

comp_11 = Contract([a1 == True, a2 == True, a3 == True], [b == True, c == True], name="comp_11")

comp_12 = Contract([a1 == True, a3 == True], [b2 == True], name="comp_12")


comp_2 = Contract([c == True], [a1 == True], name="comp_2")
comp_3 = Contract([d == True], [c == True], name="comp_3")
comp_4 = Contract([e == True], [c == True], name="comp_4")

comp_8 = Contract([m == True], [a2 == True], name="comp_8")
comp_9 = Contract([n == True, o == True], [a2 == True], name="comp_9")

comp_10 = Contract([n == True, o == True], [a1 == True, a2 == True], name="comp_10")


comp_5 = Contract([f == True], [g == True], name="comp_5")
comp_6 = Contract([h == True], [i == True], name="comp_6")
comp_7 = Contract([l == True], [m == True], name="comp_7")



contract_library.add_contracts([comp_1, comp_2, comp_3, comp_4, comp_5, comp_6, comp_7, comp_8, comp_9, comp_10, comp_11, comp_12])

# Synthesis specs
# I don't know the assumptions
spec_assumptions = []
spec_guarantees = [b == True, b2 == True]

spec_contract = Contract(spec_assumptions, spec_guarantees, name="spec_name")

# Syntehsis from contract library
list_of_contracts = contract_library.synthesize(spec_contract)

# Synthesis a new goal directly
refinement_goal = synthesize_goal(contract_library, spec_contract, "synthesised_goal")


print("\n\nAbstracted Synthesised Goal")
print(refinement_goal)

print("\nNew Goal sharing demanding some assumptions already present in the refined synthesised goal...")

goal_new = GoalModel("new_goal", [Contract([c == True], [g == True])])

satis, new_goal = compose_goals([refinement_goal, goal_new], name="top_goal")

print("\n\nNew Goal Model:")

print(new_goal)



