# HarvardX PH526X Week 4 Case Study 4 Classifying Whiskies Video 4.1.5
# Comparing Correlation Matrices
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
flavors = whisky.iloc[:, 2:14]
corr_whisky = pd.DataFrame.corr(flavors.transpose())

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
# correlations from DataFrame into numpy array
correlations = np.array(correlations)

plt.figure(figsize = (14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")
