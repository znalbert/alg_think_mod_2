# Network and Graph Resilience

These functions were used in Cousera's course Algorithmic Thinking Part 1 offered by Rice University. In this assignment, I was to analyse the resilience of a given computer network versus that of our own algorithmically generated models of a Erdős–Rényi (ER) network and UPA network.

# Network Resilience

In order to measure resilience on a network under attack we look at the largest component of the network that is still connected after the removal of a node.

# Random Attack Order

For our purposes a network was defined as resilient by having the largest connected component of nodes in the network being within 25% of the total remaining nodes. Looking at the graph below we find that all three network types meet that criterion for most of the random order attack.

[Plot of resilience under a random attack](img/random_attack_resilience.png)

# Targeted Attack Order

With the above definition for resilience we find that only the ER network is resilient up to about 20% of the nodes being removed.

[Plot of resilience under a targeted attack](img/targeted_attack_resilience.png)

# Function Runtime

We were originally given a function to generate the order of nodes to be removed under a targeted attack. However, this function was highly inefficient with a runtime on the order of O(n**2). We were instructed to create an optimized version and plot the runtimes of the two functions. The optimized function has a runtime on the order of O(n).

[Plot Runtimes of Unoptimized and Optimized Targeted Order Functions](img/function_runtimes.png)
