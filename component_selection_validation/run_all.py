from case_2_4 import *
from case_2_8 import *
from case_2_16 import *
from case_2_32 import *
from case_4_4 import *
from case_4_8 import *
from case_4_16 import *
from case_4_32 import *
from case_8_4 import *
from case_8_8 import *
from case_8_16 import *
from case_8_32 import *
from case_16_4 import *
from case_16_8 import *
from case_16_16 import *
from case_16_32 import *


if __name__ == '__main__':

	sys.stdout = open(os.devnull, 'w')
	time = run_2_4()
	sys.stdout = sys.__stdout__
	print('	2_4		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_2_8()
	sys.stdout = sys.__stdout__
	print('	2_8		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_2_16()
	sys.stdout = sys.__stdout__
	print('	2_16		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_2_32()
	sys.stdout = sys.__stdout__
	print('	2_32		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_4_4()
	sys.stdout = sys.__stdout__
	print('	4_4		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_4_8()
	sys.stdout = sys.__stdout__
	print('	4_8		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_4_16()
	sys.stdout = sys.__stdout__
	print('	4_16		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_4_32()
	sys.stdout = sys.__stdout__
	print('	4_32		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_8_4()
	sys.stdout = sys.__stdout__
	print('	8_4		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_8_8()
	sys.stdout = sys.__stdout__
	print('	8_8		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_8_16()
	sys.stdout = sys.__stdout__
	print('	8_16		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_8_32()
	sys.stdout = sys.__stdout__
	print('	8_32		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_16_4()
	sys.stdout = sys.__stdout__
	print('	16_4		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_16_8()
	sys.stdout = sys.__stdout__
	print('	16_8		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_16_16()
	sys.stdout = sys.__stdout__
	print('	16_16		' + str(time))
	sys.stdout = open(os.devnull, 'w')
	time = run_16_32()
	sys.stdout = sys.__stdout__
	print('	16_32		' + str(time))
