

import networkx as nx

G = nx.random_k_out_graph(n=8, k=2, alpha=0.75)

def draw_graph(G):
    nx.draw_circular(G, node_size=400, with_labels=True)

draw_graph(G)

ranks_pr = nx.pagerank(G)
ranks_pr

import numpy as np

def flip(p):
    return np.random.random() < p

from collections import Counter

def random_walk(G, alpha=0.85, iters=1000):
    counter = Counter()
    node = next(iter(G))

    for _ in range(iters):
        if flip(alpha):
            node = np.random.choice(list(G[node]))
        else:
            node = np.random.choice(list(G))

        counter[node] += 1

    total = sum(counter.values())
    for key in counter:
        counter[key] /= total
    return counter

ranks_rw = random_walk(G)
ranks_rw

import pandas as pd

s1 = pd.Series(ranks_pr)
s2 = pd.Series(ranks_rw)

df = pd.DataFrame(dict(PageRank=s1, RandomWalk=s2))
df['Diff'] = df['RandomWalk'] - df['PageRank']
df*100