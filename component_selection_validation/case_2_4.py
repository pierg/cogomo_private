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

contract_library.add_contracts(
    [
		Contract([p0 == True], [p1 == True], name="c0"),
		Contract([p1 == True], [p2 == True], name="c1"),
		Contract([p2 == True], [p3 == True], name="c2"),
		Contract([p3 == True], [p4 == True], name="c3")
	])

spec_a = []
spec_g = [p4 == True]

spec_contract = Contract(spec_a, spec_g, name="specification")


def run_2_4():
    t.tic()
    synthesize_goal(contract_library, spec_contract, "synthesised_goal")
    t.toc()
    return t.elapsed


if __name__ == '__main__':
    run_4_4()
