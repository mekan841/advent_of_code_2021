import numpy as np
import pandas as pd

depths = [depths]

differences = np.diff(depths)
change = []

for d in differences:
    if d > 0: change.append('increase')
    else: change.append('decrease')

change.count('increase')
