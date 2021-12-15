import pandas as pd 
import numpy as np

coords = pd.read_csv("/Users/anni/Desktop/coordinates.csv")
right = coords[coords['x']>=655]
left = coords[coords['x']<655]
split = coords['x'].max()/2
right.loc[:, "x"] = right["x"].apply(lambda t: t - split)

overlapped = right.append(left)
merged = overlapped.drop_duplicates()
len(merged)
