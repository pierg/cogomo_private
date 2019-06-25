from z3 import *
from goal_model import *
from goal_operations import *
from contract_model import *
from component_library import *


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



component_library = ComponentLibrary("cogomo")


# Components
comp_1 = Contract([a == True], [b == True], "comp_1")
comp_2 = Contract([b == True], [c == True], "comp_2")
comp_3 = Contract([c == True], [d == True], "comp_3")
comp_4 = Contract([e == True], [f == True], "comp_4")


component_library.add_contracts([comp_1, comp_2, comp_3, comp_4])

# Synthesis specs
# I don't know the assumptions
spec_assumptions = False
spec_guarantees = [a == True]

spec_contract = Contract(spec_assumptions, spec_guarantees)

synthesisted_composition = component_library.synthetise(spec_contract)


