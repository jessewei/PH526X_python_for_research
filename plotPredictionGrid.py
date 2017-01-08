import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

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

def generate_synth_data(n=50):
    """
    Create two sets of points from bivariate normal distributions.
    """
    # generate observations
    points = np.concatenate((ss.norm(0, 1).rvs((n,2)), ss.norm(1, 1).rvs((n,2))), axis=0)
    # generate outcomes
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)


if __name__ == "__main__":
    predictors, outcomes = generate_synth_data()
    print(predictors.shape)
    print(outcomes.shape)
    
    # plot KNN chart for k = 5
    k = 5; filename = "knn_synth_5.pdf"; limits = (-3, 4, -3, 4); h = 0.1
    (xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
    plot_prediction_grid(xx, yy, prediction_grid, filename)
    # plot KNN chart for k = 50
    k = 50; filename = "knn_synth_50.pdf"; limits = (-3, 4, -3, 4); h = 0.1
    (xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
    plot_prediction_grid(xx, yy, prediction_grid, filename)
    
    ## Graphs show that the borderline for k=50 is better than that for
    ## k = 5. But this does not mean that a larger k is better as it 
    ## depends on not the training dataset but real-life dataset, which
    ## the model has not seen before. This problem in choosing the appro-
    ## priate k is the Bias-Variance Tradeoff.
