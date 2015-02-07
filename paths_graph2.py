# Similar to the problem of graph 1 but this is just a recursive BFS implementation
# to slove graph 2

import itertools

graph_edges = [(0,1),(0,2),(0,3),(0,5),(1,2),(1,3),(2,3),(1,5),(2,4),(3,4)]
graph_map = {0: 'A',1: 'B',2: 'C',3: 'D',4: 'E',5: 'F'}


def find_path(graph):
             
    def freqencies():       # Find Frequencies of edges in and out of nodes
        my_list = [x for (x, y) in graph]
        result = [0 for i in range(max(my_list) + 1)]
        for i in my_list:
            result[i] += 1
        return result
         
    def find_node(tour):    # Find a node for the tour
        for i in tour:
            if freq[i] != 0:
                return i
        return -1
     
    def helper(tour, next): # This basically puts them all together
        find_path(tour, next)
        u = find_node(tour)
        while sum(freq) != 0:     
            sub = find_path([], u)
            tour = tour[:tour.index(u)] + sub + tour[tour.index(u) + 1:]  
            u = find_node(tour)
        return tour
                  
    def find_path(tour, next):  # Find a path recursively and pop that path from graph when traversed
        i, j = 0, 1
        for (x, y) in graph:
            if x == next:
                current = graph.pop(graph.index((x,y)))
                graph.pop(graph.index((current[j], current[i])))
                tour.append(current[i])
                freq[current[i]] -= 1
                freq[current[j]] -= 1
                return find_path(tour, current[j])
        tour.append(next)
        return tour             
              
    graph += [(y, x) for (x, y) in graph]
    freq = freqencies()
    return helper([], graph[0][0])

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

