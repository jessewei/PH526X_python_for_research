# HarvardX PH526x Week 3 Case Study 3: Introduction to Classification
# Video 3.3.4: Finding Nearest Neighbors

import scipy.stats as ss
import matplotlib.pyplot as plt
import numpy as np

def distance(p1, p2):
    """
    Find the distance between points p1 and p2.
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def majority_vote(votes):
    """
    Return the most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode

# loop over all points
#     compute the distance between point p and every other point
# sort distances and return those k points that are nearest to point p
# use indices = np.argsort(distances) to find the closest indices for the array distances
# use distances[indices] to call the distances of each point to p
def find_nearest_neighbors(p, points, k=5):
    """
    Find the k nearest neighbors of point p and return their indices.
    The function takes in parameters: point p, points of neighbors, and
    k, whose default is 5.
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    indices = np.argsort(distances)
    return indices[:k]


# find k nearest neighbors
# predict the class of p based on majority
def knn_predict(p, points, outcomes, k=5):
    indices = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[indices])

# initialize point p, array of points, and outcomes
points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
outcomes = np.array([0,0,0,0,1,1,1,1,1])
p = np.array([2.5, 2])

# should return 1
print(knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2))
# should return 0
print(knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2))

## Code for plotting
#plt.plot(points[:, 0], points[:, 1], "ro")
#plt.plot(p[0], p[1], "bo")
#plt.axis([0.5, 3.5, 0.5, 3.5])




