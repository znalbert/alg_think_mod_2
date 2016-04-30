"""
Algorithmic Thinking - Project 2
"""

from collections import deque


def bfs_visited(ugraph, start_node):
    """
    Undirected graph, starting node -> set of all visited nodes reached by a 
    breadth-first search from the starting node.
    """
    queue = deque([])
    visited = set([start_node])

    queue.append(start_node)

    while len(queue) > 0:
        current_node = queue.popleft()
        for neighbor in ugraph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


def cc_visited(ugraph):
    """
    Undirected graph -> list of sets of connected component nodes.
    """
    remaining_nodes = set(ugraph.keys())
    connected_components = []

    while len(remaining_nodes) > 0:
        current_node = remaining_nodes.pop()
        new_component = bfs_visited(ugraph, current_node)
        connected_components.append(new_component)
        remaining_nodes -= new_component

    return connected_components


def largest_cc_size(ugraph):
    """
    Undirected graph -> integer representing the largest connected component.
    """
    largest = 0
    for component in cc_visited(ugraph):
        if len(component) > largest:
            largest = len(component)

    return largest


def compute_resilience(ugraph, attack_order):
    """
    Undirected graph, list of nodes -> list of largest connected component
    after each node in attack order is removed.
    """
    resilience = [largest_cc_size(ugraph)]
    for node in attack_order:
        for neighbor in ugraph[node]:
            ugraph[neighbor].remove(node)
        del ugraph[node]
        resilience.append(largest_cc_size(ugraph))

    return resilience
