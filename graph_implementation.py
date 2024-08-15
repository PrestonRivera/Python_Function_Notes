import heapq



class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node, data=None):
        if node not in self.graph:
            self.graph[node] = {'data': data, 'edges': {}}
    
    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)
        
        self.graph[u]['edges'][v] = weight
        self.graph[v]['edges'][u] = weight

    def __repr__(self):
        result = ""
        for node, info in self.graph.items():
            result += f"Node: '{node}', Data: {info['data']}\n"
            for edge, weight in info['edges'].items():
                result += f"  has an edge leading to --> {edge} with weight {weight}\n"
        return result
    





def dijkstra(graph, start, end):
    # Priority queue and distances dictionary
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    parents = {start: None}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # Nodes can have multiple entries in the priority queue
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.graph[current_node]['edges'].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    # Reconstruct path from start to end
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parents.get(step)

    path.reverse()
    return path





# Example usage:
graph = Graph()


# Add nodes with additional data
graph.add_node("A", {"info": "Sugar Land"})
graph.add_node("B", {"info": "Meadows Place"})
graph.add_node("C", {"info": "Missouri City"})
graph.add_node("D", {"info": "Mission Bend"})
graph.add_node("E", {"info": "Bellaire"})
graph.add_node("F", {"info": "Southside Place"})
graph.add_node("G", {"info": "Houston"})

# Add edges (connections) between nodes
graph.add_edge("A", "B", 24)
graph.add_edge("B", "C", 18)
graph.add_edge("C", "D", 6)
graph.add_edge("D", "E", 18)
graph.add_edge("E", "F", 16)
graph.add_edge("F", "G", 2)


print(graph)  # Displays nodes with their data and connections

# Example usage:
shortest_path = dijkstra(graph, "A", "G")
print("Shortest path from A to B:", shortest_path)