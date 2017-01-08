from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import random

# Homemade Algorithms for KNN: 7 Functions
def distance(p1, p2):
    """
    Find the distance between points p1 and p2.
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

# Note that for this video the professor uses majority_vote_long()
# instead of majority_vote_short()
def majority_vote(votes):
    """
    Return the most common element in votes.
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    
    return random.choice(winners)

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

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)




if __name__ == "__main__":
    iris = datasets.load_iris()

    # take all rows but only columns 0 and 1
    predictors = iris.data[:, 0:2]
    # take the dataset's classfication label
    outcomes = iris.target

    ## plot and save the graph for different outcomes
    #plt.plot(predictors[outcomes==0][:, 0], predictors[outcomes==0][:, 1], "ro")
    #plt.plot(predictors[outcomes==1][:, 0], predictors[outcomes==1][:, 1], "go")
    #plt.plot(predictors[outcomes==2][:, 0], predictors[outcomes==2][:, 1], "bo")
    #plt.savefig("iris.pdf")

    ## plot prediction and save the graph
    #k = 5; filename = "iris_grid.pdf"; limits = (4, 8, 1.5, 4.5); h = 0.1
    #(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
    #plot_prediction_grid(xx, yy, prediction_grid, filename)

    # use sklearn.neighbors KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 5)
    knn.fit(predictors, outcomes)
    sk_predictions = knn.predict(predictors)
    # use homemade algorithm
    my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])
    #print(my_predictions)
    print("sk_predictions == my_predictions?: ", sk_predictions == my_predictions)
    print("% of same results between sk_predictions and my_predictions: ", 100 * np.mean(sk_predictions == my_predictions))
    print("% of sk_predictions same to outcomes: ", 100 * np.mean(sk_predictions == outcomes))
    print("% of my_predictions same to outcomes: ", 100 * np.mean(my_predictions == outcomes))
