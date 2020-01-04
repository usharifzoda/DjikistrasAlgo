import Vertexes

g = Vertexes.Graph()

vertex_a = Vertexes.Vertex("New York")
vertex_b = Vertexes.Vertex("Tokyo")
vertex_c = Vertexes.Vertex("London")

g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)

g.add_directed_edge(vertex_a, vertex_b, 8)
g.add_directed_edge(vertex_b, vertex_c, 12)

print(g)