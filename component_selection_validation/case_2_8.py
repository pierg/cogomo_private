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

contract_library.add_contracts(
    [
		Contract([p0 == True], [p1 == True], name="c0"),
		Contract([p1 == True], [p2 == True], name="c1"),
		Contract([p2 == True], [p3 == True], name="c2"),
		Contract([p3 == True], [p4 == True], name="c3"),
		Contract([p4 == True], [p5 == True], name="c4"),
		Contract([p5 == True], [p6 == True], name="c5"),
		Contract([p6 == True], [p7 == True], name="c6"),
		Contract([p7 == True], [p8 == True], name="c7")
	])

spec_a = []
spec_g = [p8 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_2_8():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_2_8()
