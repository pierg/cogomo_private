from z3 import *
from contracts.contract_library import *

# Contants:
Delta_m = 1  # meters
RSSI_net = 60  # dbm
Epsilon_d = 1
D_platoon = 10  # platooning distance
D_safe = 20  # safety distance

# Variables

velocity_ego_t = Real('velocity_ego_t')    # current speed of the vehicle, at time t
velocity_ego_t1 = Real('velocity_ego_t1')  # speed of the ego vehicle at time t+1
steering_ego = Real('steering_ego')

velocity_lea = Real('velocity_lea')
steering_lea = Real('steering_lea')

distance_front = Real('distance_front')  # measured distance
distance_real = Real('distance_real')

sig_network = Bool('sig_network')  # network ON
connected_platoon = Bool('connected_platoon')
sig_rssi = Real('sig_rssi')
sig_radar = Bool('sig_radar')
sig_gps = Bool('sig_gps')
latitude = Real('latitude')
longitude = Real('longitude')
position_x = Real('position_x')
position_network = Real('position_network')

radar_accuracy = Real('radar_accuracy')
gps_accuracy = Real('gps_accuracy')

ang_gas = Real('ang_gas')
break_req = Real('break_req')
acc_ego = Real('acc_ego')


contract_library = ContractLibrary("cogomo")

accelerometer = Contract(velocity_ego_t > 0, acc_ego > 0, "accelerometer")
gps_sensor_1 = Contract(sig_gps == True, [latitude > 0, longitude > 0, gps_accuracy == 3], "gps_sensor_1")
gps_sensor_2 = Contract(sig_gps == True, [latitude > 0, longitude > 0, gps_accuracy == 2], "gps_sensor_2")
gps_sensor_3 = Contract(sig_gps == True, [latitude > 0, longitude > 0, gps_accuracy == 5], "gps_sensor_3")
kalman_filter = Contract([acc_ego > 0, latitude > 0, longitude > 0, gps_accuracy > 2], position_x > 0, "kalman_filter")
radar_1 = Contract(sig_radar == True, [distance_front > 0, radar_accuracy == 22], "radar_1")
radar_2 = Contract(sig_radar == True, [distance_front > 0, radar_accuracy == 18], "radar_2")
network = Contract(sig_network == True, position_network > 0, "network")
sensor_fusion = Contract([position_x > 0, position_network > 0, distance_front > 0, radar_accuracy > 20],
                         [Implies(distance_front > distance_real, (distance_front - distance_real) < Delta_m),
                          Implies(distance_front <= distance_real, (distance_real - distance_front) <= Delta_m)], "sensor_fusion")

contract_library.add_contracts([accelerometer,
                                gps_sensor_1,
                                gps_sensor_2,
                                gps_sensor_3,
                                kalman_filter,
                                radar_1,
                                radar_2,
                                network,
                                sensor_fusion])