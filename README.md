# Dijkstra's Algorithm with NetworkX

## Basic Requirements

- Python 3.x
- NetworkX library (pip install networkx)

## **About Dijkstra's Algorithm**

Dijkstra's algorithm is a graph search algorithm that finds the shortest path between nodes in a graph with non-negative edge weights. It operates by iteratively exploring nodes from a start node outward, updating the shortest distance to each node as it progresses.

## **Code 1: Hardcoded Graph**

This Python script demonstrates Dijkstra's algorithm with a hardcoded graph using the NetworkX library.
- networkx is imported to utilize its functions for graph creation and manipulation.
- An empty graph G is created using nx.Graph().
- Edges with specified weights are added to the graph using G.add_edge().
- Dijkstra's algorithm is applied using nx.shortest_path() and nx.shortest_path_length() to find the shortest path and its distance.
- The result is printed, showing the shortest path and total distance.

## **Code 2: User Input Graph**

This Python script demonstrates Dijkstra's algorithm with a user-input graph using the NetworkX library.
- networkx is imported to utilize its functions for graph creation and manipulation.
- An empty graph G is created using nx.Graph().
- The user inputs the number of edges and details of each edge, including start node, end node, and weight.
- Dijkstra's algorithm is applied using nx.shortest_path() and nx.shortest_path_length() to find the shortest path and its distance.
- The result is printed, showing the shortest path and total distance.

## **How Dijkstra's Algorithm Works**

Dijkstra's algorithm operates by maintaining a priority queue of nodes to explore, initially containing only the start node. It iteratively explores nodes in order of increasing distance from the start node, updating the shortest distance to each node as it progresses. This process continues until the destination node is reached or all reachable nodes have been explored.

