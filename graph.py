class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def insert(self, vertex, edge, is_bidirectional):
        if not vertex in self.graph:
            self._insert(vertex)
        
        if not edge in self.graph:
            self._insert(edge)
        
        self.graph.get(vertex).append(edge)
        if is_bidirectional:
            self.graph.get(edge).append(vertex)
    
    def display(self):
        for key, values in self.graph.items():
            print(key, ": ", *values)


    def _insert(self, data):
        self.graph[data] = []

graph = Graph()

graph.insert('c', 't', True)
graph.insert('c', 'f', True)
graph.insert('f', 'g', False)

graph.display()
