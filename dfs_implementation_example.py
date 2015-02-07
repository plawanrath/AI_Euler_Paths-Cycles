#This file shows how DFS can be used to find the solutions to both (a) and (b)
#I have created this file to demonstrate DFS to solve the problem since, I am
#finding all solutions using BFS technique and I thought one demonstration
#of DFS to do the same was necessary.

graph = {'A': ['B','C','D','F'],
'B': ['A','C','D','F'],
'C': ['B','E','D','A'],
'D': ['A','B','C','E'],
'E': ['D','C'],
'F': ['A','B']}

nodes = ['A','B','C','D','E','F']

graph1 = {'A': ['D','C','B'],
'B': ['A','D','C'],
'C': ['B','A','D','E'],
'D': ['A','B','C','E'],
'E': ['D','C']}

nodes1 = ['A','B','C','D','E']

# Get The frequencies of edges coming in or out from any node

def degrees(graph,nodes):
  freq = []
  for node in nodes:
    freq.insert(nodes.index(node),0)
  for v1 in graph:
    for v2 in graph[v1]:
      freq[nodes.index(v2)] += 1
  return freq

# Get all edges of the graph

def getAllEdges(graph):
  res = []
  for v1 in graph:
    for v2 in graph[v1]:
      res.append((v1,v2))
  return res

# Relevent Data structures

nodeVisited = []
edgesVisited = []
stack = []

def push(stack,source):
  stack.append(source)

# This function will push a bunch of items into the stack

def pushList(stack,list):
  for val in list:
    stack.append(val)

# This function will return a list containing all the children nodes that
# can be traversed from any node.

def getChildren(graph,node):
  res = []
  for nd in graph[node]:
    if (node,nd) not in edgesVisited:
      res.append(nd)
  return res   

# Note: This is a check which I borrowed from Euler's Theorem to
# check in advance, if there can be a straight line from A to A 
# or if there can be any such line from A to anywhere covering
# every vertex

def checkPathOrCycle(graph,nodes):
  odd_nodes = 0
  no_of_nodes = degrees(graph,nodes)
  for nd in no_of_nodes:
    if nd % 2 == 1:
      odd_nodes += 1
  if odd_nodes == 2:
    print "No paths from A to A"
  elif odd_nodes == 0:
    print "No Paths from A to anywhere else"
  else:
    print "No Paths"

# DFS implementation this has been explained in the paperwork..
  
def dfs(graph,source):
  push(stack,source)
  lastNode = None
  while len(edgesVisited) != len(allEdges) and stack:
    if nodeVisited:
      lastNode = nodeVisited[-1]
    node = stack.pop()
    nodeVisited.append(node)
    if lastNode:
      edgesVisited.append((node,lastNode))
      edgesVisited.append((lastNode,node))
    child = getChildren(graph,node)
    pushList(stack,child)
  if len(edgesVisited) == len(allEdges):
    print nodeVisited  


checkPathOrCycle(graph1,nodes1)
allEdges = getAllEdges(graph1)
dfs(graph1,'A')

nodeVisited[:] = []
edgesVisited[:] = []
stack[:] = []
checkPathOrCycle(graph,nodes)
allEdges = getAllEdges(graph)
dfs(graph,'A')

