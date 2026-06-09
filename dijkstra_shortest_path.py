# Weighted graph represented as an adjacency list
# Each tuple contains (neighbor, edge_weight)
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def shortest_path(graph, start, target=''):
    """
    Compute shortest paths from a starting node using Dijkstra's algorithm.

    Args:
        graph (dict): weighted graph represented as adjacency list
        start (str): starting node
        target (str): optional destination node

    Returns:
        distances (dict): shortest distance from start to every node
        paths (dict): shortest path from start to every node
    """

    # List of nodes that have not been visited yet
    unvisited = list(graph)

    # Initialize distances:
    # start node = 0
    # all other nodes = infinity
    distances = {
        node: 0 if node == start else float('inf')
        for node in graph
    }

    # Store shortest paths
    paths = {node: [] for node in graph}
    paths[start].append(start)

    # Main Dijkstra loop
    while unvisited:

        # Select unvisited node with smallest known distance
        current = min(unvisited, key=distances.get)

        # Explore all neighbors of current node
        for node, distance in graph[current]:

            # Check if a shorter path has been found
            if distance + distances[current] < distances[node]:

                # Update shortest distance
                distances[node] = distance + distances[current]

                # Update shortest path
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])

                paths[node].append(node)

        # Mark current node as visited
        unvisited.remove(current)

    # Print either one target or all nodes
    targets_to_print = [target] if target else graph

    for node in targets_to_print:

        # Skip the starting node
        if node == start:
            continue

        print(
            f'\n{start}-{node} distance: {distances[node]}'
            f'\nPath: {" -> ".join(paths[node])}'
        )

    return distances, paths


# Example: shortest path from A to F
shortest_path(my_graph, 'A', 'F')
