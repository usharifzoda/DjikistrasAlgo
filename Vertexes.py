class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    def __init__(self):
        self.adjacncy_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacncy_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacncy_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)