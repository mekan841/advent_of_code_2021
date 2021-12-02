import pandas as pd 
import numpy as np

#First Puzzle 

dive_example = pd.read_csv("/Users/anni/Desktop/dive_example.csv")
dive_grouped = dive_example.groupby('Direction')['Metres'].sum()

dive_grouped['up'] = dive_grouped['up']*-1

vertical_distance = dive_grouped['up']+dive_grouped['down']

multiplier = dive_grouped['forward']*vertical_distance
print (multiplier)

