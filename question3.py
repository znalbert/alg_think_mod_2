"""
Question 3
"""

import time
import assignment2 as a
import matplotlib.pyplot as plt

# Implement fast_targeted_order

# Analyze running time of targeted_order and fast_targeted_order on UPA graphs
# of size n and m = 5. Analysis should be both mathematical and empirical and 
# include:
# - Determine big-O bounds for worst-case running times of both functions
# - Compute a plot comparing the running times of both functions:
# -- n = range(10, 1000, 10) and m = 5.


def fast_targeted_order(ugraph):
    """ dict -> list
    Takes a graph and outputs an ordered list of of nodes is descending order
    of their degree.
    """
    degree_sets = {}
    num_nodes = len(ugraph)
    for node in range(0, num_nodes):
        degree_sets[node] = set([])

    for node_degree in range(0, num_nodes):
        degree = len(ugraph[node_degree])
        degree_sets[degree].add(node_degree)

    desc_node_degrees = []
    index = 0

    for degree in range(num_nodes - 1, -1, -1):
        while len(degree_sets[degree]) > 0:
            node_to_add = degree_sets[degree].pop()
            for neighbor in ugraph[node_to_add]:
                neighbor_degree = len(ugraph[neighbor])
                degree_sets[neighbor_degree].remove(neighbor)
                degree_sets[neighbor_degree - 1].add(neighbor)
            desc_node_degrees.insert(index, node_to_add)
            index += 1
            a.delete_node(ugraph, node_to_add)

    return desc_node_degrees


def running_times(function):
    times = []
    for graph_size in range(10, 1000, 10):
        graph = a.make_upa_graph(graph_size, 5)
        start_time = time.time()
        function(graph)
        end_time = time.time()
        times.append(end_time - start_time)

    return times


def plot_runtimes(fto_times, to_times):
    """
    Plot an example with two curves with legends
    """
    graph_sizes = range(10, 1000, 10)

    plt.plot(graph_sizes, fto_times, '-b', label='fast_targeted_order')
    plt.plot(graph_sizes, to_times, '-r', label='targeted_order')

    plt.legend(loc='upper left')
    plt.ylabel('Run Time')
    plt.xlabel('UPA Graph Size')
    plt.grid(True)
    plt.title('Comparison of Function Run Times\nPython Desktop Environment\n')
    plt.show()


fto = running_times(fast_targeted_order)
to = running_times(a.targeted_order)

plot_runtimes(fto, to)
