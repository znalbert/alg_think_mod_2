"""
Algorithmic Thinking - Assignment 2
"""

from collections import deque

def bfs_visited(ugraph, start_node):
    """ dict -> set
    Takes an undirected graph represented by a dictionary and a starting node
    and returns a set of all visited nodes reached by a breadth-first search
    from the starting node.
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
    """ dict -> list
    Takes a dictionary representation of an undirected graph and returns a
    list of sets of connected component nodes.
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
    """ dict -> int
    Takes a dictionary representation of an undirected graph and returns an
    integer representing the largest connected component.
    """
    largest = 0
    for component in cc_visited(ugraph):
        if len(component) > largest:
            largest = len(component)

    return largest


def compute_resilience(ugraph, attack_order):
    """ dict, list -> list
    Takes a dictionary representation of an undirected graph and a list of
    nodes and returns a list of largest connected component after each node
    in attack order is removed.
    """
    resilience = []
    for node in attack_order:
        for neighbor in ugraph[node]:
            ugraph[neighbor].remove(node)
        del ugraph[node]
        resilience.append(largest_cc_size(ugraph))

    return resilience


"""
Graph Operations from Assignment 1
"""

def make_complete_graph(num_nodes):
    """ int -> dict
    Takes an integer and returns a dictionary of a complete digraph containing
    that many nodes.
    """
    graph = {}
    for node in range(0, num_nodes):
        connections = range(0, num_nodes)
        connections.remove(node)
        graph[node] = set(connections)

    return graph


def compute_in_degrees(digraph):
    """ dict -> dict
    Takes a digraph represented as a dictionary, and returns a dictionary in 
    which the keys are the nodes and the values are the nodes' indegree value.
    """
    indegrees = {}
    for node in digraph:
        indegrees[node] = 0
    for node in digraph:
        for edge in digraph[node]:
            indegrees[edge] += 1

    return indegrees


def in_degree_distribution(digraph):
    """ dict -> dict
    Takes a digraph dictionary object, and returns a dictionary of the degrees,
    and values being the number of nodes with that degree.
    """
    degrees = {}

    node_indegrees = compute_in_degrees(digraph)
    for node in node_indegrees:
        degree = node_indegrees[node]
        if degree in degrees:
            degrees[degree] += 1
        else:
            degrees[degree] = 1

    return degrees


def compute_out_degrees(digraph):
    """ dict -> dict
    Takes a directed graph represented as a dictionary, and returns a dictionary
    in which the keys are the nodes and the values are the nodes' outdegree
    value.
    """
    out_degrees = {}
    for node in digraph:
        out_degrees[node] = len(digraph[node])

    return out_degrees


def avg_out_degree(out_degree_dict):
    """ dict -> int
    Takes a dictionary of node keys and their outdegree values and an interger
    representing the number of nodes, and returns the average outdegree.
    """
    total_out_degree = 0
    for node in out_degree_dict:
        total_out_degree += out_degree_dict[node]

    return float(total_out_degree)/len(out_degree_dict)


def normalized_in_degree(in_degree_dict):
    """ dict -> dict
    Takes a dictionary of nodes with their indegree value, and returns a 
    normalized dictionary whose values sum up to 1.
    """
    normalized = {}
    for key in in_degree_dict:
        normalized[key] = float(in_degree_dict[key]) / len(in_degree_dict)
    return normalized

