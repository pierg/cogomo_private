from case_4_4 import *


if __name__ == '__main__':

    sys.stdout = open(os.devnull, 'w')
    time = run_4_4()
    sys.stdout = sys.__stdout__
    print(run_4_4())

