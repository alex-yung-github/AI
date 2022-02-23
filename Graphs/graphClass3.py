
class Graph(object): #had ot make them lists because it is a directed graph and the arrows are only one way. Sets would make the arrows randomly pointed
    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if(len(graph_dict) > 0):
            self.graphD = graph_dict
        else:
            self.graphD = {}
       
        #TODO

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        if(vertice not in self.graphD):
            raise Exception("vertex does not exist")
        return self.graphD[vertice]
        #TODO
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        temp = []
        for i in self.graphD:
            temp.append(i)
        return temp
        #TODO

    def all_edges(self):
        edges = []
        for i in self.graphD:
            for j in self.graphD[i]:
                if([i, j] not in edges):
                    edges.append([i, j])
        return edges

        #TODO

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if(vertex not in self.graphD):
            self.graphD[vertex] = {}
        #TODO
    def delete_vertex(self, vertex):
        self.graphD.pop(vertex)
        for i in self.graphD:
            if(vertex in self.graphD[i]):
                self.graphD[i].pop(vertex)
    def delete_edge(self, start, end):
        self.graphD[start].pop(end)
    def change_weight(self, start, end, newweight):
        self.graphD[start][end] = newweight
    def add_edge(self, edge, value): #made it so that it is only from edge element 1 to edge element 2 to instead of both ways
                            #not sure if this is the correct way, but i can fix it if it isnt the right way
       
        x = iter(edge)
        temp1 = next(x)
        temp2 = next(x)
        if(temp1 not in self.graphD):
            self.add_vertex(temp1)
        if(temp2 not in self.graphD):
            self.add_vertex(temp2)
        if(temp2 not in self.graphD[temp1]):
            self.graphD[temp1] = ({temp2 : value})
        


        
        # #TODO

    def generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        for i in self.graphD:
            for j in self.graphD[i]:
                print(i + ", " + j)

        #TODO
    
    def __iter__(self):
        self._iter_obj = iter(self.graphD)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self.graphD:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res

g = {"A" : {"B" : 3},
        "B" : {"C" : 2, "D" : 4}, 
        "C" : {"E" : 5},
        "D" : {"C" : 5},
        "E" : {"D" : 2}
                    }
                    
graph = Graph(g)
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print("Add vertex:")
graph.add_vertex("J")

print("Add an edge:")
graph.add_edge(["G", "H"], 20)

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print("Showing edges with values")
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print('Adding an edge {"Z","X"} with new vertices and a value of 22:')
graph.add_edge({"Z","X"}, 22)
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())

print('Adding an edge {"H", "B"} with new vertices and a value of 12:')
graph.add_edge(["H","B"], 12)
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())

print("Showing new edges with values")
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

graph.delete_vertex("D")

print("Showing new edges with values")
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("Changing weight from H to B to 29")
graph.change_weight("H", "B", 29)

print("Showing new edges with values")
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("Remove edge G to H")
graph.delete_edge("G", "H")

print("Showing new edges with values")
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

