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
p61 = Bool('p61')
p62 = Bool('p62')
p63 = Bool('p63')
p64 = Bool('p64')
p65 = Bool('p65')
p66 = Bool('p66')
p67 = Bool('p67')
p68 = Bool('p68')
p69 = Bool('p69')
p70 = Bool('p70')
p71 = Bool('p71')
p72 = Bool('p72')
p73 = Bool('p73')
p74 = Bool('p74')
p75 = Bool('p75')
p76 = Bool('p76')
p77 = Bool('p77')
p78 = Bool('p78')
p79 = Bool('p79')
p80 = Bool('p80')
p81 = Bool('p81')
p82 = Bool('p82')
p83 = Bool('p83')
p84 = Bool('p84')
p85 = Bool('p85')
p86 = Bool('p86')
p87 = Bool('p87')
p88 = Bool('p88')
p89 = Bool('p89')
p90 = Bool('p90')
p91 = Bool('p91')
p92 = Bool('p92')
p93 = Bool('p93')
p94 = Bool('p94')
p95 = Bool('p95')
p96 = Bool('p96')

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
		Contract([p45 == True, p46 == True], [p47 == True, p48 == True], name="c15"),
		Contract([p48 == True, p49 == True], [p50 == True, p51 == True], name="c16"),
		Contract([p51 == True, p52 == True], [p53 == True, p54 == True], name="c17"),
		Contract([p54 == True, p55 == True], [p56 == True, p57 == True], name="c18"),
		Contract([p57 == True, p58 == True], [p59 == True, p60 == True], name="c19"),
		Contract([p60 == True, p61 == True], [p62 == True, p63 == True], name="c20"),
		Contract([p63 == True, p64 == True], [p65 == True, p66 == True], name="c21"),
		Contract([p66 == True, p67 == True], [p68 == True, p69 == True], name="c22"),
		Contract([p69 == True, p70 == True], [p71 == True, p72 == True], name="c23"),
		Contract([p72 == True, p73 == True], [p74 == True, p75 == True], name="c24"),
		Contract([p75 == True, p76 == True], [p77 == True, p78 == True], name="c25"),
		Contract([p78 == True, p79 == True], [p80 == True, p81 == True], name="c26"),
		Contract([p81 == True, p82 == True], [p83 == True, p84 == True], name="c27"),
		Contract([p84 == True, p85 == True], [p86 == True, p87 == True], name="c28"),
		Contract([p87 == True, p88 == True], [p89 == True, p90 == True], name="c29"),
		Contract([p90 == True, p91 == True], [p92 == True, p93 == True], name="c30"),
		Contract([p93 == True, p94 == True], [p95 == True, p96 == True], name="c31")
	])

spec_a = []
spec_g = [p96 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_4_32():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_4_32()
