# HarvardX PH526X Week 4 Case Study 4 Classifying Whiskies Video 4.1.4
# Cluster Whiskies by Flavor Profile
import pandas as pd
import numpy as np
from sklearn.cluster.bicluster import SpectralCoclustering

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
flavors = whisky.iloc[:, 2:14]
corr_whisky = pd.DataFrame.corr(flavors.transpose())

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
print(model.rows_)

print(np.sum(model.rows_, axis=1))
print(np.sum(model.rows_, axis=0))
print(model.row_labels_)
