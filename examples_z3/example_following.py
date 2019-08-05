# Copyright (c) Microsoft Corporation 2015, 2016

# The Z3 Python API requires libz3.dll/.so/.dylib in the 
# PATH/LD_LIBRARY_PATH/DYLD_LIBRARY_PATH
# environment variable and the PYTHONPATH environment variable
# needs to point to the `python' directory that contains `z3/z3.py'
# (which is at bin/python in our binary releases).

# If you obtained example.py as part of our binary release zip files,
# which you unzipped into a directory called `MYZ3', then follow these
# instructions to run the example:

# Running this example on Windows:
# set PATH=%PATH%;MYZ3\bin
# set PYTHONPATH=MYZ3\bin\python
# python example.py

# Running this example on Linux:
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:MYZ3/bin
# export PYTHONPATH=MYZ3/bin/python
# python example.py

# Running this example on macOS:
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:MYZ3/bin
# export PYTHONPATH=MYZ3/bin/python
# python example.py


from z3 import *

s = Solver()


# Contants:
D_platoon = 15      # meters
delta_m = 1         # meter
RSSI_net = 60   # dbm
V_i = 50



# Variables
d_front = Real('d_front')
d_real = Real('d_real')
v_ego = Real('v_ego')
s_ego = Real('s_ego')
s_network = Bool('s_network')   # network ON
s_rssi = Real('s_rssi')
v_leader = Real('v_leader')
s_leader = Real('s_leader')

# C1
a_1 = [True]
g_1 = [(d_front > 0), Implies(d_front > d_real, (d_front - d_real) < delta_m), Implies(d_front <= d_real, (d_real - d_front) <= delta_m)]

# C2
a_2 = [d_front != D_platoon]
g_2 = [v_ego == V_i]

# C3
a_3 = [s_network, s_rssi > RSSI_net]
g_3 = [v_leader >= 0, s_leader <= 1, s_leader >= -1]

# C4
a_4 = [v_leader >= 0, s_leader <= 1, s_leader >= -1]
g_4 = [v_ego == v_leader, s_ego == s_leader]



# Composition
g_comp = g_1 + g_2 + g_3 + g_4

for g_elem in g_comp:
    s.assert_and_track(g_elem, str(g_elem))


print s.assertions()
print(s.check())
print(s.model())
