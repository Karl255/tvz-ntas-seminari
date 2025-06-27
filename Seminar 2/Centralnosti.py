import math
from collections import deque
import numpy as np


def degree_centrality(graph):
    """
    Calculate degree centrality for each node.
    Degree centrality is simply the number of connections a node has.
    """
    centrality = {}
    max_degree = len(graph) - 1  # maximum possible degree
    for node in graph:
        degree = len(graph[node])
        centrality[node] = degree / max_degree if max_degree > 0 else 0
    return centrality


def closeness_centrality(graph):
    """
    Calculate closeness centrality for each node.
    Closeness centrality is the inverse of the average shortest path distance to all other nodes.
    """
    centrality = {}
    nodes = list(graph.keys())
    n = len(nodes)

    for node in nodes:
        # BFS to calculate shortest paths to all other nodes
        distances = {n: -1 for n in nodes}
        distances[node] = 0
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if distances[neighbor] == -1:  # not visited yet
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        total_distance = sum(distances.values())
        if total_distance > 0:
            centrality[node] = (n - 1) / total_distance
        else:
            centrality[node] = 0

    return centrality


def betweenness_centrality(graph):
    """
    Calculate betweenness centrality for each node.
    Betweenness centrality measures how often a node appears on shortest paths between other nodes.
    """
    nodes = list(graph.keys())
    centrality = {node: 0 for node in nodes}

    for s in nodes:
        # BFS from source node s
        pred = {node: [] for node in nodes}  # predecessors
        dist = {node: -1 for node in nodes}  # distances
        sigma = {node: 0 for node in nodes}  # number of shortest paths
        sigma[s] = 1
        dist[s] = 0
        queue = deque([s])
        stack = []

        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in graph[v]:
                if dist[w] == -1:  # first time seeing w
                    dist[w] = dist[v] + 1
                    queue.append(w)
                if dist[w] == dist[v] + 1:  # shortest path to w via v
                    sigma[w] += sigma[v]
                    pred[w].append(v)

        delta = {node: 0 for node in nodes}
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                centrality[w] += delta[w]

    # Normalize the centrality values
    n = len(nodes)
    if n > 2:
        scale = 1 / ((n - 1) * (n - 2))
        centrality = {k: v * scale for k, v in centrality.items()}

    return centrality


def eigenvector_centrality(graph, max_iter=100, tol=1.0e-6):
    """
    Calculate eigenvector centrality for each node.
    Eigenvector centrality measures a node's importance based on the importance of its neighbors.
    """
    nodes = list(graph.keys())
    n = len(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}

    # Create adjacency matrix
    adj_matrix = np.zeros((n, n))
    for node in nodes:
        for neighbor in graph[node]:
            adj_matrix[node_index[node]][node_index[neighbor]] = 1

    # Power iteration
    x = np.ones(n) / n  # initial vector
    for _ in range(max_iter):
        x_new = adj_matrix @ x
        x_new = x_new / np.linalg.norm(x_new, 2)
        if np.linalg.norm(x_new - x, 2) < tol:
            break
        x = x_new

    centrality = {nodes[i]: x[i] for i in range(n)}
    return centrality

def centralnosti(graph):
    print("Degree Centrality:", degree_centrality(graph))
    print("Closeness Centrality:", closeness_centrality(graph))
    print("Betweenness Centrality:", betweenness_centrality(graph))
    print("Eigenvector Centrality:", eigenvector_centrality(graph))