class Graph(object): #had ot make them lists because it is a directed graph and the arrows are only one way. Sets would make the arrows randomly pointed
    def __init__(self, graphD=None, vertices=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if(len(graphD) > 0):
            self.graphD = graphD
            self.vertices = vertices
        else:
            self.graphD = []
            self.vertices = []
       
        #TODO

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        if(vertice not in self.vertices):
            raise Exception("vertex does not exist")
        return self.graphD[self.vertices.index(vertice)]
        #TODO
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        temp = []
        for i in self.vertices:
            temp.append(i)
        return temp
        #TODO

    def all_edges(self):
        edges = []
        for i in range(len(self.graphD)):
            for j in range(len(self.graphD)):
                if(self.graphD[i][j] == 1):
                    edges.append([self.vertices[i], self.vertices[j]])
        return edges

        #TODO

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        vertex = int(vertex)
        if(vertex not in self.vertices):
            self.graphD.append([0 for i in self.vertices])
            self.vertices.append(vertex)
            for i in range(len(self.graphD)):
                self.graphD[i].append(0)
        
        #TODO
    def delete_vertex(self, vertex):
        x = self.vertices.index(vertex)
        print(x)
        for i in self.graphD:
            i.pop(x)
        self.graphD.pop(x)
        self.vertices.remove(vertex)
    def delete_edge(self, start, end):
        x = self.vertices.index(start)
        y = self.vertices.index(end)
        self.graphD[x][y] = 0
    def change_weight(self, start, end, weight):
        x = self.vertices.index(start)
        y = self.vertices.index(end)
        if(self.graphD[x][y] > 0):
            self.graphD[x][y] = weight
    def add_edge(self, edge): 
        x = iter(edge)
        temp1 = int(next(x))
        temp2 = int(next(x))
        if(temp1 not in self.graphD):
            self.add_vertex(temp1)
        if(temp2 not in self.graphD):
            self.add_vertex(temp2)
        index1 = self.vertices.index(temp1)
        index2 = self.vertices.index(temp2)
        if(self.graphD[index1][index2] == 0):
            self.graphD[index1][index2] = 1
        


        
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
    # def find_path (self, start, end, path_so_far=[]):
    #     path_so_far.append(start)
    #     if(self.graphD[self.vertices.index(start)][self.vertices.index(end)] == 1):
    #         path_so_far.append(end)
    #         return(path_so_far)
    #     else:
    #         for i in self.graphD[self.vertices.index(start)]:
    #             if(i == 1):
                    
            
                    
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

g = [[0, 1, 0, 0],
     [0, 0, 0, 1],
     [1, 0, 0, 1],
     [0, 1, 0, 0]
                ]
verts = [1, 2, 3, 4]
graph = Graph(g, verts)
for vertice in graph.vertices:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print("Add vertex:")
graph.add_vertex(4)

print("Add an edge:")
graph.add_edge([4, 3])

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print('Adding an edge {"20","53"} with new vertices:')
graph.add_edge([20, 53])
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())

print('Adding an edge {"-1","53"} with new vertices:')
graph.add_edge(["-1","53"])
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())

print("Graph: ")
for vertice in graph.vertices:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("deleting edge -1 to 53")
graph.delete_edge(-1, 53)

print("Graph: ")
for vertice in graph.vertices:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("deleting vertex 53")
graph.delete_vertex(53)

print("Graph: ")
for vertice in graph.vertices:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

print("changing weight of 4 to 2 to 5 weight")
graph.change_weight(4, 2, 5)

print("Graph: ")
for vertice in graph.vertices:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))
