"""
Provided code for Application portion of Module 2
"""

import urllib2
import random
import time
import math
import matplotlib.pyplot as plt
import upa_trial as upa
import graph_operations as go

############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

##########################################################
# My code


def make_er_graph(num_nodes, probability):
    """ int, int -> dict
    Takes an integer and a probabilty and returns a dictionary of a
    complete digraph containing that many nodes.
    """
    graph = {}
    for node in range(0, num_nodes):
        graph[node] = set([])

    for node in range(0, num_nodes - 1):
        for potential_neighbor in range(node + 1, num_nodes):
            if random.random() < probability:
                graph[node].add(potential_neighbor)
                graph[potential_neighbor].add(node)

    return graph


def make_upa_graph(nodes, out_degree):
    """ int, int -> dict
    Takes a number of nodes and average out-degreee of those nodes, and returns
    a dictionary representing the graph of the UPA algorithm with those values.
    """
    graph = go.make_complete_graph(out_degree)
    trial = upa.UPATrial(out_degree)
    for new_node in range(out_degree, nodes):
        neighbors = trial.run_trial(out_degree)
        graph[new_node] = neighbors
        for neighbor in neighbors:
            graph[neighbor].add(new_node)
    return graph


def check_undirected(graph):
    for node in graph:
        for neighbor in graph[node]:
            if node not in graph[neighbor]:
                return False
    return True


def check_number_edges(ugraph):
    directed_edges = 0
    for node in ugraph:
        directed_edges += len(ugraph[node])
    if directed_edges % 2 == 0:
        return directed_edges / 2
    else:
        return "Not Undirected"

def random_order(ugraph):
    """ dict -> list
    Takes a dictionary representation of a graph and returns the nodes as a 
    randomly sorted list.
    """
    nodes = ugraph.keys()
    ro_nodes = []
    while len(nodes) > 0:
        choices = range(0, len(nodes))
        random_node = nodes.pop(random.choice(choices))
        ro_nodes.append(random_node)

    return ro_nodes


def plot_resiliences(nodes, network_vals, er_vals, upa_vals):
    """
    Plot an example with two curves with legends
    """
    node_vals = range(0, nodes)

    plt.plot(node_vals, network_vals, '-b', label='Network')
    plt.plot(node_vals, er_vals, '-r', label='ER')
    plt.plot(node_vals, upa_vals, '-g', label='UPA')

    plt.legend(loc='upper right')
    plt.ylabel('Size of Largest Connected Component')
    plt.xlabel('Number of Nodes Removed')
    plt.grid(True)
    plt.title('Comparison of Graph Resilience\nMeasured by Largest Connected Component vs Nodes Removed by Target Attack\n')
    plt.show()


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
