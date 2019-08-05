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


print "~~~~~ Refinement Check ~~~~~~"
x, y, z = Ints('x y z')

s1 = Function('S1', IntSort(), BoolSort())
s2 = Function('S2', IntSort(), BoolSort())

# s.add(Implies(p1, And(x < 5, x > -2)))
# s.add(Implies(p2, And(y < 4)))


s.assert_and_track(ForAll(x, If(And(x < 5, x > 3), s1(x) == True, s1(x) == False)), "x < 5")
s.assert_and_track(ForAll(y, If(And(y < 4, y > -2), s2(y) == True, s2(y) == False)), "x < 4")

s.add(ForAll(y, Implies(s2(y), s1(y))))

print s.check()
print s.unsat_core()