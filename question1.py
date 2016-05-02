"""
Question 1
"""

import assignment2 as a
import graph_operations as go
import matplotlib.pyplot as plt

# Find probability p such that the ER graph will have approximately the
# same number of edges as the computer network.

NODES = 1239
EDGES = 3047
NETWORK_GRAPH = a.load_graph(a.NETWORK_URL)

# EDGE_PROB is probability p for ER graph
POSS_EDGES = float(NODES) * (NODES - 1) / 2
EDGE_PROB = float(EDGES) / POSS_EDGES

er_graph = a.make_er_graph(NODES, EDGE_PROB)

# AVG_OUTDEGREE is m for the UPA graph
OUTDEGREE_DICT = go.compute_out_degrees(NETWORK_GRAPH)
HALF_AVG_OUTDEGREE = int(round(go.avg_out_degree(OUTDEGREE_DICT) / 2))

upa_graph = a.make_upa_graph(NODES, HALF_AVG_OUTDEGREE)

network_random = a.random_order(NETWORK_GRAPH)
er_random = a.random_order(er_graph)
upa_random = a.random_order(upa_graph)

network_resilience = go.compute_resilience(a.copy_graph(NETWORK_GRAPH), network_random)
er_resilience = go.compute_resilience(a.copy_graph(er_graph), er_random)
upa_resilience = go.compute_resilience(a.copy_graph(upa_graph), upa_random)


print "Network Edges:", EDGES
print "Network undirected:", a.check_undirected(NETWORK_GRAPH)
print "Check Network Edges:", a.check_number_edges(NETWORK_GRAPH)
print "res len:", len(network_resilience)

print "\nER info:"
print "p:", EDGE_PROB
print "er undirected:", a.check_undirected(er_graph)
print "Number edges:", a.check_number_edges(er_graph)
print "er res len:", len(er_resilience)

print "\nUPA info:"
print "m:", HALF_AVG_OUTDEGREE
print "upa undirected:", a.check_undirected(upa_graph)
print "Number UPA Edges:", a.check_number_edges(upa_graph)
print "upa res len:", len(upa_resilience)

def plot_resiliences(nodes, network_vals, er_vals, upa_vals):
    """
    Plot an example with two curves with legends
    """
    node_vals = range(0, nodes)

    plt.plot(node_vals, network_vals, '-b', label='Network')
    plt.plot(node_vals, er_vals, '-r', label='ER: p = ' + str(EDGE_PROB))
    plt.plot(node_vals, upa_vals, '-g', label='UPA: m = ' + str(HALF_AVG_OUTDEGREE))

    plt.legend(loc='upper right')
    plt.ylabel('Size of Largest Connected Component')
    plt.xlabel('Number of Nodes Removed')
    plt.grid(True)
    plt.title('Comparison of Graph Resilience\nMeasured by Largest Connected Component vs Randomly Removed Nodes\n')
    plt.show()

plot_resiliences(NODES, network_resilience, er_resilience, upa_resilience)


