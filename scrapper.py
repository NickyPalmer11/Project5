from subprocess import run
from matplotlib import pyplot as plt
import re, sys
from time import time
# Regular expression patterns declarations
PATTERN_TOOK = re.compile(r'Took\s.*\sseconds')
PATTERN_GOAL = re.compile(r'Goal\sTime:\s.*\sseconds')

# Pulling some functions out to make life easier
write = sys.stdout.write
flush = sys.stdout.flush

# Matplotlib setup for notebook
%matplotlib inline
# Run the simulation for a range of stations
for i in range(10, 101, 5):
    start = time()
    write(f"{i} Stations now running...")
    flush()
    result = run(["python3", "project.py", str(i), "10", "100", "YourMac"], capture_output=True).stdout.decode("utf-8", "ignore")
    write(f"done!")
    stop = time()
    write(f"{i} Stations took {(stop - start)/1000} seconds\n")
    actual = float(PATTERN_TOOK.search(result).group(0).split()[1])
    goal = float(PATTERN_GOAL.search(result).group(0).split()[2])
    flush()
    file.write(f"{i},{actual},{goal}\n")
    file.flush()
print("Done!")
file.close()
# Use the generated file to plot the data
file = open('output.csv', 'r')
stations = []
took = []
goal = []
for line in file:
    stations.append(int(line.split(',')[0]))
    took.append(float(line.split(',')[1]))
    goal.append(float(line.split(',')[2]))
file.close()
plt.plot(stations, took, label='Actual runtime')
plt.plot(stations, goal, label='Goal runtime')
plt.legend()
plt.xlabel('Number of stations')
plt.ylabel('Runtime (seconds)')
plt.show()
