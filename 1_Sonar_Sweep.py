#First Puzzle

import numpy as np
import pandas as pd

depths = [depths]

differences = np.diff(depths)
change = []

for d in differences:
    if d > 0: change.append('increase')
    else: change.append('decrease')

change.count('increase')


#Second Puzzle
triple_sums = [depths[i] + depths[i+1] + depths[i+2] for i in range(len(depths)-2)]

triple_differences = np.diff(triple_sums)
triple_change = []

for d in triple_differences:
    if d > 0: triple_change.append('increase')
    else: triple_change.append('decrease')

triple_change.count('increase')
