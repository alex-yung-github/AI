
from typing import List, Set


def findEdges(graph):
    edges = []
    for i in graph:
        for j in graph[i]:
            if({i, j} not in edges):
                edges.append({i, j})
    return edges
def add_vertex(graphD, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if(vertex not in graphD):
            graphD[vertex] = []
def findIsolatedNotes(graph):
    isolated = []
    for node in graph:
        if(not graph[node]):
            isolated.append(node)
    return isolated
graph = {"a" : {"c"},
        "b" : {"c", "e"}, 
        "c" : {"a", "b", "d", "e"},
        "d" : {"e"},
        "e" : {"c", "b"},
        "f" : {}       
                    }
edge = ["g", "d"]

# templist = []
# if(type(edge) == 'set'):
#     for i in edge:
#         templist.append(i)
#     edge = templist
# if(edge[0] not in graph):
#     add_vertex(graph, edge[0])
# if(edge[1] not in graph):
#     add_vertex(graph, edge[1])
# graph[edge[1]].append(edge[0])
# graph[edge[0]].append(edge[1])


# if("g" not in graph):
#             graph["g"] = []
# temp = []
# for i in graph:
#     temp.append(i)
# print(temp)
print(findEdges(graph))
print(findIsolatedNotes(graph))
print(graph)