import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

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
    n = 20
    points, outcomes = generate_synth_data(n)
    
    plt.figure()
    plt.plot(points[:n, 0], points[:n, 1], "ro")
    plt.plot(points[n:, 0], points[n:, 1], "bo")
    plt.savefig("bivardata.pdf")
