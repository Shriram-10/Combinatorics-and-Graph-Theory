# Graph Theory Assignment
* This program demonstrates several key graph theory algorithms and functionalities, including graph generation using the Havel-Hakimi algorithm, detecting Eulerian circuits with Fleury's algorithm, and finding shortest paths using Dijkstra's algorithm. The program also explores minimum spanning trees, fundamental cutsets, circuits, and measures graph connectivity.

## Features

### Graph Generation (Havel-Hakimi Algorithm):
* The program generates a valid graphical sequence (a sequence of node degrees) and constructs a graph using the Havel-Hakimi algorithm. The user can either input their own graphical sequence or let the program generate one randomly.
* The generated graph is displayed visually, and the structure is verified for correctness.

### Eulerian Circuit Detection (Fleury's Algorithm):
* The program checks if the graph is Eulerian (i.e., all nodes have even degrees).
* If the graph is Eulerian, it finds an Eulerian circuit using Fleury's algorithm and displays the circuit path.

### Assigning Random Weights to Edges:
* Random weights are assigned to the edges of the graph. These weights are displayed on the graph for visualization.

### Shortest Path (Dijkstra's Algorithm):
* The program computes the shortest path from a random starting node to all other nodes using Dijkstra's algorithm. The shortest paths and their lengths are displayed.

### Minimum Spanning Tree (Kruskal's Algorithm):
* The program computes and displays the minimum spanning tree (MST) of the graph using Kruskal's algorithm.
* The MST edges are highlighted in red in the graphical representation.

### Fundamental Cutsets and Circuits:
* Fundamental cutsets and circuits with respect to the minimum spanning tree are computed and displayed.

### Graph Connectivity:
* The program computes both edge connectivity and vertex connectivity of the graph, and determines the K-connectedness of the graph.
