import os
import sys


print('cwd', os.getcwd())
run = int(sys.argv[1])


command = 'python3 grid_search.py '
command2 = 'python3 plotting.py '

# choose scenario
if run <= 11:
    input = '1 ' + str(run)
elif run <= 22:
    input = '2 ' + str(run)

os.system(command + input)

