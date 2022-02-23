class Graph(object):
    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if(len(graph_dict) > 0):
            self.graphD = graph_dict
        else:
            self.graphD = set()
       
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
                if({i, j} not in edges):
                    edges.append({i, j})
        return edges

        #TODO

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if(vertex not in self.graphD):
            self.graphD[vertex] = set()
        #TODO

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        for i in edge:
            for s in edge:
                temp1 = i
                temp2 = s
                if(temp1 not in self.graphD):
                    self.add_vertex(temp1)
                if(temp2 not in self.graphD):
                    self.add_vertex(temp2)
                if(temp2 not in self.graphD[temp1]):
                    self.graphD[temp1].add(temp2)
                if(temp1 not in self.graphD[temp2]):
                    self.graphD[temp2].add(temp1)
        #Method to addedge if for example you wanted to add_edge("ab","fg") and you wanted to connect a and b together and f and g together
        # for i in edge:
        #     for s in range(len(i)-1):
        #         temp1 = i[s:s+1]
        #         for s2 in range(s+1, len(i)):
        #             temp2 = i[s2:s2+1]
        #             if(temp1 not in self.graphD):
        #                 self.add_vertex(temp1)
        #             if(temp2 not in self.graphD):
        #                 self.add_vertex(temp2)
        #             if(temp2 not in self.graphD[temp1]):
        #                 self.graphD[temp1].add(temp2)
        #             if(temp1 not in self.graphD[temp2]):
        #                 self.graphD[temp2].add(temp1)


        
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


g = {"a" : {"d"},
        "b" : {"c"}, 
        "c" : {"c", "d", "b", "e"},
        "d" : {"c", "a"},
        "e" : {"c"},
        "f" : set()
                    }
                    
graph = Graph(g)
for vertice in graph:
    print(f"Edges of vertex {vertice}: ", graph.edges(vertice))

graph.add_edge({"ab", "fg"})
graph.add_edge({"xyz", "bla"})

print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print("Add vertex:")
graph.add_vertex("z")

print("Add an edge:")
graph.add_edge({"a", "d"})

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.all_vertices())
print("Edges of graph:")
print(graph.all_edges())
