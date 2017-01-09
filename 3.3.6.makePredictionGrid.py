import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

def majority_vote(votes):
    """
    Return the most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode

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

def knn_predict(p, points, outcomes, k=5):
    """
    Classify point p among points using the K-Nearest_Neighbor method.
    """
    indices = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[indices])

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """
    Classify each point on the prediction grid.
    """
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    
    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)
    return (xx, yy, prediction_grid)
