# HarvardX PH526X Week 4 Video 4.1.2 Loading and Inspecting Data
# Requires two txt files: regions.txt and whiskies.txt
import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

# peeking the DataFrame
print(whisky.head())
print(whisky.iloc[0:10])

# check column names
print(whisky.columns)
# get all data related to flavors: all rows, columns 2-13
flavors = whisky.iloc[:, 2:14]
print(flavors.head())

# peek rows 5-10 and columns 0-5
print(whisky.iloc[5:10, 0:5])
