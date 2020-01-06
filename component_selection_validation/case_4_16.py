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
p25 = Bool('p25')
p26 = Bool('p26')
p27 = Bool('p27')
p28 = Bool('p28')
p29 = Bool('p29')
p30 = Bool('p30')
p31 = Bool('p31')
p32 = Bool('p32')
p33 = Bool('p33')
p34 = Bool('p34')
p35 = Bool('p35')
p36 = Bool('p36')
p37 = Bool('p37')
p38 = Bool('p38')
p39 = Bool('p39')
p40 = Bool('p40')
p41 = Bool('p41')
p42 = Bool('p42')
p43 = Bool('p43')
p44 = Bool('p44')
p45 = Bool('p45')
p46 = Bool('p46')
p47 = Bool('p47')
p48 = Bool('p48')

contract_library.add_contracts(
    [
		Contract([p0 == True, p1 == True], [p2 == True, p3 == True], name="c0"),
		Contract([p3 == True, p4 == True], [p5 == True, p6 == True], name="c1"),
		Contract([p6 == True, p7 == True], [p8 == True, p9 == True], name="c2"),
		Contract([p9 == True, p10 == True], [p11 == True, p12 == True], name="c3"),
		Contract([p12 == True, p13 == True], [p14 == True, p15 == True], name="c4"),
		Contract([p15 == True, p16 == True], [p17 == True, p18 == True], name="c5"),
		Contract([p18 == True, p19 == True], [p20 == True, p21 == True], name="c6"),
		Contract([p21 == True, p22 == True], [p23 == True, p24 == True], name="c7"),
		Contract([p24 == True, p25 == True], [p26 == True, p27 == True], name="c8"),
		Contract([p27 == True, p28 == True], [p29 == True, p30 == True], name="c9"),
		Contract([p30 == True, p31 == True], [p32 == True, p33 == True], name="c10"),
		Contract([p33 == True, p34 == True], [p35 == True, p36 == True], name="c11"),
		Contract([p36 == True, p37 == True], [p38 == True, p39 == True], name="c12"),
		Contract([p39 == True, p40 == True], [p41 == True, p42 == True], name="c13"),
		Contract([p42 == True, p43 == True], [p44 == True, p45 == True], name="c14"),
		Contract([p45 == True, p46 == True], [p47 == True, p48 == True], name="c15")
	])

spec_a = []
spec_g = [p48 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_4_16():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_4_16()
