from contract_library import *
from contracts.contract_model import *

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



component_library = ContractLibrary("cogomo")


# Components
comp_1 = Contract([a1 == True, a2 == True], [b == True], "comp_1")

comp_11 = Contract([a1 == True, a2 == True, a3 == True], [b == True, c == True], "comp_11")

comp_12 = Contract([a1 == True, a3 == True], [b2 == True], "comp_12")



comp_2 = Contract([c == True], [a1 == True], "comp_2")
comp_3 = Contract([d == True], [c == True], "comp_3")
comp_4 = Contract([e == True], [c == True], "comp_4")

comp_8 = Contract([m == True], [a2 == True], "comp_8")
comp_9 = Contract([n == True, o == True], [a2 == True], "comp_9")

comp_10 = Contract([n == True, o == True], [a1 == True, a2 == True], "comp_10")


comp_5 = Contract([f == True], [g == True], "comp_5")
comp_6 = Contract([h == True], [i == True], "comp_6")
comp_7 = Contract([l == True], [m == True], "comp_7")



component_library.add_contracts([comp_1, comp_2, comp_3, comp_4, comp_5, comp_6, comp_7, comp_8, comp_9, comp_10, comp_11, comp_12])

# Synthesis specs
# I don't know the assumptions
spec_assumptions = [False]
spec_guarantees = [b == True, b2 == True]

spec_contract = Contract(spec_assumptions, spec_guarantees)

synthesisted_composition = component_library.synthetise(spec_contract)


