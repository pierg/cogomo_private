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
p49 = Bool('p49')
p50 = Bool('p50')
p51 = Bool('p51')
p52 = Bool('p52')
p53 = Bool('p53')
p54 = Bool('p54')
p55 = Bool('p55')
p56 = Bool('p56')
p57 = Bool('p57')
p58 = Bool('p58')
p59 = Bool('p59')
p60 = Bool('p60')

contract_library.add_contracts(
    [
		Contract([p0 == True, p1 == True, p2 == True, p3 == True, p4 == True, p5 == True, p6 == True, p7 == True], [p8 == True, p9 == True, p10 == True, p11 == True, p12 == True, p13 == True, p14 == True, p15 == True], name="c0"),
		Contract([p15 == True, p16 == True, p17 == True, p18 == True, p19 == True, p20 == True, p21 == True, p22 == True], [p23 == True, p24 == True, p25 == True, p26 == True, p27 == True, p28 == True, p29 == True, p30 == True], name="c1"),
		Contract([p30 == True, p31 == True, p32 == True, p33 == True, p34 == True, p35 == True, p36 == True, p37 == True], [p38 == True, p39 == True, p40 == True, p41 == True, p42 == True, p43 == True, p44 == True, p45 == True], name="c2"),
		Contract([p45 == True, p46 == True, p47 == True, p48 == True, p49 == True, p50 == True, p51 == True, p52 == True], [p53 == True, p54 == True, p55 == True, p56 == True, p57 == True, p58 == True, p59 == True, p60 == True], name="c3")
	])

spec_a = []
spec_g = [p60 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_16_4():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_16_4()
