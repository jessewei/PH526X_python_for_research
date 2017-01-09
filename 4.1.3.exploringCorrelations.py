# HarvardX PH526X Week 4 Case Study 4 Classifying Whiskies Video 4.1.3
# Finding Correlations between sweetness and honey, using Pearson Correlation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

# get all data related to flavors: all rows, columns 2-13
flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

plt.figure(figsize=(10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10, 10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")
