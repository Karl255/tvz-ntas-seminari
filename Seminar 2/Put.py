class Put:
    def __init__(self, odrediste, udaljenost, pb, oznaka=None):
        self.odrediste = odrediste
        self.udaljenost = udaljenost
        self.pb = pb
        self.oznaka = oznaka
        self.trajanje = udaljenost/pb
        self.short = self.odrediste[0] + self.odrediste[1]
    def __str__(self):
        return self.odrediste

    def __repr__(self):
        return self.short


""" Razred Graph() i popratne slike preuzeti sa stranice:
https://www.python-course.eu/graphs_python.php
"""


class Graph(object):

    def __init__(self, graph_dict=None):
        """ inicijalizacija objekta:
            ako ništa nije predano inicijalizira se prazna struktura rječnika
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ vraća listu bridova za neki vrh"""
        return self._graph_dict[vertice]

    def all_vertices(self):
        """ vraća vrhove grafa """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ vraća bridove grafa """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ dodavanje novog vrha """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ dodavanje brida """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].append(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ metoda za dobivanje liste bridova grafa """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj

    def __next__(self):
        """ pomoćna metoda za iteriranje kroz vrhove """
        return next(self._iter_obj)

    def __str__(self):
        res = "vrhovi: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nrubovi: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """ pronalaženje puta između dva vrha """
        if path == None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ pronalaženje svih puteva između dva vrha """
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        """ vraća stupanj vrha """
        degree = len(self._graph_dict[vertex])
        if vertex in self._graph_dict[vertex]:
            degree += 1
        return degree

    def find_isolated_vertices(self):
        """ vraća listu izoliranih vrhova """
        graph = self._graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def Delta(self):
        """ najveći stupanj između svih vrhova """
        max = 0
        for vertex in self._graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def degree_sequence(self):
        """ vraća sekvencu stupnjeva """
        seq = []
        for vertex in self._graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    def density(self):
        """ izračun gustoće grafa """
        g = self._graph_dict
        V = len(g.keys())
        E = len(self.all_edges())
        return (2.0 * E) / (V * (V - 1))

    def diameter(self):
        """ izračun dijametra grafa"""

        v = tuple(self.all_vertices())
        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1]) - 1
        return diameter

