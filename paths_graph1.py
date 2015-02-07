# This is a BFS implementation to find paths from A to A covering all edges and 
# paths from A to any other edges covering all edges, whichever is present in the
# given graph.
# NOTE: Just for convenienve, I am giving two copies of this same file, one with
# graph 1 and the other with graph 2. Just for ease of understanding. 

# Another modification to BFS made here is that, I have turned the graph itself into the tree
# meaning, I will directly keel removing edges from graph in a breadth first manner. This I have
# done because python has the facilities to easily generate possible combinations of values and
# using that feature with the idea, I would be saving a lot of space in BFS implementation.

import itertools
def find_path(graph):
 
    # The number of edges in the graph
    edges = len(graph)
 
    # Create a dictionary with the degree of each node
    degrees = {}
 
    for edge in graph:
        for node in edge:
            if node in degrees:
                degrees[node] += 1
            else:
                degrees[node] = 1
 
    # Determine how many nodes have odd degree
    odd_nodes = 0
    for node in degrees:
        if degrees[node] % 2 == 1:
            odd_nodes += 1
 
    # Return None if the graph doesn't contain a path.
    # A graph only has a path if the number of nodes
    # with odd degree is 0 or 2 (Euler Theorem)
    if odd_nodes != 2 and odd_nodes != 0:
        return None
 
    # A list of the steps of the path
    path = []
 
    # If there are odd nodes, the path must start with an odd node
    for node in degrees:
        if degrees[node] % 2 == 1:
            # Start with an arbitrary path, not necessarily Eulerian
            # The first and final nodes have odd degree
            path = find_arbitrary_path(graph, node)
            break

    # If there are no odd nodes, start with an arbitrary node
    if len(path) == 0:
        path = find_arbitrary_path(graph, graph[0][0])
 
    # If the current path does not contain all nodes, there are missing inner, closed paths
    while len(path) < (edges + 1):
 
        # Determine a node which has missing edges in the path
        current_node = None
        for node in path:
            if degrees[node] > (path.count(node) + 1):
                current_node = node
                break
 
        # The index of this node in the path
        node_index = path.index(current_node)
        # An arbitrary, closed path containing the node with the remaining edges
        inner_path = find_arbitrary_path(graph, current_node)
        # Add the closed path to the current path
        path = path[:node_index] + inner_path + path[node_index + 1:]
 
    return path
 
 
# Finds an arbitrary path from a given starting node. If the starting
# node has odd degree, the path will end with a node of odd degree.
# Otherwise,the path will be closed. The used edges are removed from
# the graph variable.
 
def find_arbitrary_path(graph, starting_node):
 
    path = [starting_node]
 
    # If there are unused edges, find edges connected to the last node
    # and add the connected node to the path
    while len(graph):
 
        for i in range(len(graph)):
            if graph[i][0] == path[-1]:
                path.append(graph[i][1])
                graph.pop(i)
                break
            elif graph[i][1] == path[-1]:
                path.append(graph[i][0])
                graph.pop(i)
                break
            # If there are no such edges, the path can't be continued
            # and is returned
            elif i == len(graph) - 1:
                return path
 
    # If all edges have been used, return the path
    return path
 
# This is done since its much simpler to work with numbers
 
graph_edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(2,4),(3,4)]
graph_map = {0: 'A',1: 'B',2: 'C',3: 'D',4: 'E'}


d = range(0,len(graph_edges))
count = 0
for item in graph_edges:
  if item[0] == 0:
    count += 1

e = len(d)
val = []
for p in itertools.permutations(d, e):
  if p[0] in range(0,count):
    graph = []
    for v in p:
      graph.append(graph_edges[v])
    val1 = find_path(graph)
    if val1 not in val:
      val.append(val1)
      res = []
      for x in val1:
        res.append(graph_map[x])
      print res

