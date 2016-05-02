"""
Question 4
"""

import assignment2 as a
import graph_operations as go
import question1 as g

net_graph = g.NETWORK_GRAPH
er_graph = g.er_graph
upa_graph = g.upa_graph

net_targets = a.targeted_order(a.copy_graph(net_graph))
er_targets = a.targeted_order(a.copy_graph(er_graph))
upa_targets = a.targeted_order(a.copy_graph(upa_graph))

net_resilience = go.compute_resilience(net_graph, net_targets)
er_resilience = go.compute_resilience(er_graph, er_targets)
upa_resilience = go.compute_resilience(upa_graph, upa_targets)

a.plot_resiliences(g.NODES, net_resilience, er_resilience, upa_resilience)


