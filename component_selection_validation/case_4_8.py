from contracts.contract_library import *
from goal_model import *
from ttictoc import TicToc

t = TicToc()

contract_library = ContractLibrary("cogomo")

p0 = Bool('p0')
p1 = Bool('p1')
p2 = Bool('p2')
p3 = Bool('p3')
p4 = Bool('p4')
p5 = Bool('p5')
p6 = Bool('p6')
p7 = Bool('p7')
p8 = Bool('p8')
p9 = Bool('p9')
p10 = Bool('p10')
p11 = Bool('p11')
p12 = Bool('p12')
p13 = Bool('p13')
p14 = Bool('p14')
p15 = Bool('p15')
p16 = Bool('p16')
p17 = Bool('p17')
p18 = Bool('p18')
p19 = Bool('p19')
p20 = Bool('p20')
p21 = Bool('p21')
p22 = Bool('p22')
p23 = Bool('p23')
p24 = Bool('p24')

contract_library.add_contracts(
    [
		Contract([p0 == True, p1 == True], [p2 == True, p3 == True], name="c0"),
		Contract([p3 == True, p4 == True], [p5 == True, p6 == True], name="c1"),
		Contract([p6 == True, p7 == True], [p8 == True, p9 == True], name="c2"),
		Contract([p9 == True, p10 == True], [p11 == True, p12 == True], name="c3"),
		Contract([p12 == True, p13 == True], [p14 == True, p15 == True], name="c4"),
		Contract([p15 == True, p16 == True], [p17 == True, p18 == True], name="c5"),
		Contract([p18 == True, p19 == True], [p20 == True, p21 == True], name="c6"),
		Contract([p21 == True, p22 == True], [p23 == True, p24 == True], name="c7")
	])

spec_a = []
spec_g = [p24 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_4_8():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_4_8()
