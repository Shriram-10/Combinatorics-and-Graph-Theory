import networkx as nx
import matplotlib.pyplot as plt
import random
from typing import List, Dict, Tuple


def generate_graphic_sequence(n: int) -> List[int]:
    """Generate a random graphical sequence that is valid."""
    sequence = [random.randint(0, n-1) for _ in range(n)]
    while not nx.is_graphical(sequence):
        sequence = [random.randint(0, n-1) for _ in range(n)]
    return sequence


def havel_hakimi(sequence: List[int]) -> nx.Graph:
    """Create a graph from a valid graphic sequence using Havel-Hakimi algorithm."""
    if not nx.is_graphical(sequence):
        return None

    G = nx.Graph()
    nodes = list(range(len(sequence)))
    
    while sequence and max(sequence) > 0:
        sequence, nodes = zip(*sorted(zip(sequence, nodes), reverse=True))
        sequence = list(sequence)
        nodes = list(nodes)

        d = sequence.pop(0)
        v = nodes.pop(0)

        if d > len(sequence):
            return None

        for i in range(d):
            sequence[i] -= 1
            if sequence[i] < 0:
                return None
            G.add_edge(v, nodes[i])

    return G


def is_eulerian(G: nx.Graph) -> bool:
    """Check if the graph is Eulerian (all nodes have even degree)."""
    return nx.is_eulerian(G)


def fleury_algorithm(G: nx.Graph) -> List[Tuple[int, int]]:
    """Implement Fleury's algorithm to find Eulerian circuit."""
    if not is_eulerian(G):
        return []

    G_copy = G.copy()
    eulerian_path = list(nx.eulerian_circuit(G_copy))
    return eulerian_path


def assign_random_weights(G: nx.Graph) -> None:
    """Assign random weights to the edges of the graph."""
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)


def dijkstra(G: nx.Graph, start: int) -> Dict[int, int]:
    """Implement Dijkstra's algorithm for shortest path."""
    return nx.single_source_dijkstra_path_length(G, start, weight='weight')


def minimum_spanning_tree(G: nx.Graph) -> nx.Graph:
    """Find minimum spanning tree using Kruskal's algorithm."""
    return nx.minimum_spanning_tree(G)


def fundamental_cutsets(G: nx.Graph, T: nx.Graph) -> List[set]:
    """Find fundamental cutsets with respect to the spanning tree."""
    cutsets = []
    for edge in G.edges():
        if edge not in T.edges():
            T.add_edge(*edge)
            cutset = nx.minimum_edge_cut(T, *edge)
            cutsets.append(cutset)
            T.remove_edge(*edge)
    return cutsets


def fundamental_circuits(G: nx.Graph, T: nx.Graph) -> List[set]:
    """Find fundamental circuits with respect to the spanning tree."""
    circuits = []
    for edge in G.edges():
        if edge not in T.edges():
            T.add_edge(*edge)
            circuit = nx.find_cycle(T, edge)
            circuits.append(set(circuit))
            T.remove_edge(*edge)
    return circuits


def edge_connectivity(G: nx.Graph) -> int:
    """Find edge connectivity of the graph."""
    return nx.edge_connectivity(G)


def vertex_connectivity(G: nx.Graph) -> int:
    """Find vertex connectivity of the graph."""
    return nx.node_connectivity(G)


def k_connectedness(G: nx.Graph) -> int:
    """Find the K-connectivity of the graph."""
    return min(edge_connectivity(G), vertex_connectivity(G))


def main():
    choice = input("Enter Y to input your own graphic sequence, or any other key for random generation: ")
    
    if choice.lower() == 'y':
        n = int(input("Enter the length of the graphic sequence: "))
        sequence = [0, -1]
        while not nx.is_graphical(sequence):
            sequence.clear()
            sequence = [int(input(f"Degree of node {i}: ")) for i in range(n)]
            if not nx.is_graphical(sequence):
                print("The entered sequence is not graphical. Try again.")
    else:
        n = random.randint(5, 10)
        sequence = generate_graphic_sequence(n)

    print("Generated sequence:", sequence)
    G = havel_hakimi(sequence)
    
    if G is None:
        print("Failed to generate a valid graph.")
        return
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')
    plt.title("Generated Graph using Havel-Hakimi Algorithm")
    plt.savefig("generated_graph.png")
    plt.show()

    if is_eulerian(G):
        print("The graph is Eulerian.")
        euler_circuit = fleury_algorithm(G.copy())
        print("Euler circuit:", euler_circuit)
    else:
        print("The graph is not Eulerian.")

    assign_random_weights(G)
    start_node = random.choice(list(G.nodes()))
    shortest_paths = dijkstra(G, start_node)
    print(f"Shortest paths from node {start_node}:", shortest_paths)
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Weighted Graph with Random Weights")
    plt.savefig("weighted_graph.png")
    plt.show()

    T = minimum_spanning_tree(G)
    cutsets = fundamental_cutsets(G, T)
    circuits = fundamental_circuits(G, T)

    print("Fundamental cutsets:", cutsets)
    print("Fundamental circuits:", circuits)

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold')
    nx.draw_networkx_edges(T, pos, edge_color='r', width=2)
    plt.title("Minimum Spanning Tree (in red)")
    plt.savefig("minimum_spanning_tree.png")
    plt.show()

    edge_conn = edge_connectivity(G)
    vertex_conn = vertex_connectivity(G)
    k_conn = k_connectedness(G)

    print("Edge connectivity:", edge_conn)
    print("Vertex connectivity:", vertex_conn)
    print("The graph is K-connected for K =", k_conn)


if __name__ == "__main__":
    main()
