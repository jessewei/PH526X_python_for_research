import random
import scipy.stats as ss

def majority_vote_long(votes):
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

def majority_vote_short(votes):
    """
    Return the most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode

votes = [1,2,3,1,2,3,1,2,3,3,3,3]
winners_long = majority_vote_long(votes)
winners_short = majority_vote_short(votes)
print(winners_long, winners_short)
    
