def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]

    # creating adjacency list
    # v is the vertex and u is the adjacent vertices that determines the degree
    for v in graph[u]:
        if visited_edge[u][v] == False:  # checks if the vertices u, v are not visited
            visited_edge[u][v], visited_edge[v][u] = True, True  # follows that the vertices are unvisited;

            path = dfs(v, graph, visited_edge, path)
    return path


# checking if graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:  # checking if the nodes have even degrees
            odd_degree_nodes += 1  # count the number of odd nodes
            odd_node = i
    print(f"Number of odd nodes:{odd_degree_nodes}")
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("Graph not a Euler circuit")
        print("Reason: It has no path and a odd node degree")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path or semi-Eulerian")
        print("Reason: Has two odd node degree")
    if check == 1:
        print("Graph has a Euler Circuit")
        print("Reason: Has zero odd node degree ")
    path = dfs(start_node, graph, visited_edge)
    print(path)


def main():
    G1 = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [4]
    }
    G2 = {
        1: [2, 3, 4, 5],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5],
        5: [1, 4]
    }
    G3 = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2],
        4: [1, 2, 5],
        5: [4]
    }
    G4 = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
    }
    G5 = {
        1: [],
        2: []

    }
    max_node = 10
    check_euler(G1, max_node)
    check_euler(G2, max_node)
    check_euler(G3, max_node)
    check_euler(G4, max_node)
    check_euler(G5, max_node)


if __name__ == "__main__":
    main()

    """Determining the probability"""

    """
    To determine the probability of a given graph to be Eulerian, the following conditions must be met:
        1. The graph must have even node degrees. The probability that the nodes have even node degree is 1/2.
        2. The graph must be connected. The probability the the graph is connected is 1/2. W can therefore calculate 
        the probability of the given graph being the we know the probability of it being connected. 

    So, the probability that any given graph has a Eulerian circuit is is given by the above conditions.
            P(Euler) = P(even node degree) * P(graph is connected)
                     = 1/2 * 1/2
                     = 0.25 or 25%
    """
