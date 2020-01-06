from goal_model import *
from contracts.contract_model import *
from case_study_variables import *


a_measure_distance = []             # The designer doesn't know the assumptions
g_measure_distance = [(distance_front > 0),
                      Implies(distance_front > distance_real, (distance_front - distance_real) < Delta_m),
                      Implies(distance_front <= distance_real, (distance_real - distance_front) <= Delta_m)]


synthesized_measure_distance = synthesize_goal(contract_library, Contract(a_measure_distance, g_measure_distance),
                                               "measure_distance_synth")