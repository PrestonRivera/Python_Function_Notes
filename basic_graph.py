
class Graph:
    def __init__(self):
        self.graph = {}

    # Breadth first search(BFS)
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        vertex = v
        to_visit.append(vertex)

        while len(to_visit) != 0:
            s = to_visit.pop(0) # s = current vertex being processed
            visited.append(s)
            sorted_neighbors = sorted(self.graph[s])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited


    def bfs_path(self, start, end):
        predecessor = {}
        to_visit = []
        visited = []
        shortest_path = []
        to_visit.append(start)

        while len(to_visit) != 0:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbors = sorted(self.graph[s])
            
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    predecessor[neighbor] = s
                    if neighbor == end:
                        current = end
                        while current is not None:
                            shortest_path.append(current)
                            current = predecessor.get(current)
                        shortest_path.reverse()
                        return shortest_path
        return None


    # Depth first search(DFS)
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited
     

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbors in sorted_neighbors:
            if neighbors not in visited:
                self.depth_first_search_r(visited, neighbors)


    def unconnected_vertices(self):
        unconnected = []
        for vertex, connections in self.graph.items():
            if not connections:
                unconnected.append(vertex)
        return unconnected


    def adjacent_nodes(self, node):
        if node not in self.graph:
            return []
        return list(self.graph[node])


    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}
            

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
    

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
    


graph = Graph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
graph.add_edge("E", "C")

print(graph)

path = graph.bfs_path("A", "E")

print(path)




