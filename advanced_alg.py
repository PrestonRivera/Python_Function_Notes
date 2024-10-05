### ADVANCED ALGORITHMS COURSE


# Dijkstra's Algorithm

'''
Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm) is an algorithm for finding the shortest paths between vertices in a graph. For example, 
I may want to find the shortest path along a road network for my daughter's paper route.


Dijkstra's Algorithm is a weighted graph algorithm. It's used to find the shortest path between two vertices in a weighted graph.


Weighted Graphs
A weighted graph is a graph whose edges have a "weight" or "cost". The weight of an edge can represent distance, time, or anything that models the "cost of traversing" the pair of vertices it connects.
'''


'''
Dijkstra's Algorithm starts at a source vertex and traverses the graph to find the shortest path between the source and a destination.
The algorithm keeps track of the "shortest distance so far" while it travels and it updates it each time it finds a shorter path.
Once all of a node's neighbors have been checked and their distances have been updated, that node is marked as visited.
The process continues until all the vertices in the graph have been visited. By the end, the final path connects the root to the destination following the shortest path possible.
'''


def dijkstra(graph, src, dest):
    # Create an empty set for unvisited nodes
    unvisited = set()
    # Create a dict to keep track of the paths we are traversing
    predecessors = {}
    # Create empty dict to keep track of the shortest known distance from src to each node
    distances = {}
    # Iterate through the nodes in the graph (adjacency list)
    for node in graph:
        # Add all the nodes to the unvisited set
        unvisited.add(node)
        # If the node equals the src (the key of the current node)
        if node == src:
            # Set the distance to src node to 0
            distances[node] = 0
        else:
            # Set the distance to all other nodes to positive infinity
            distances[node] = float("inf")
    # Start a while loop that ends when no nodes left in unvisited
    while unvisited:
        # Get the node with the min dist from src node using helper function 
        min_dist_node = get_min_dist_node(distances, unvisited)
        # Remove that node from the unvisited set
        unvisited.remove(min_dist_node)
        # If that node is the destination 
        if min_dist_node == dest:
            # Return the full path from src to destination using helper function 
            return get_path(dest, predecessors)
        else:
            # Iterate through the unvisited neighbor nodes of min_dist_node
            for neighbor in graph[min_dist_node]:
                # Check if that neighbor node is unvisited
                if neighbor in unvisited:
                    # Calculate the dist to the neighbor node through min_dist_node
                    distance_through_min_dist_node = distances[min_dist_node] + graph[min_dist_node][neighbor]
                    # Compare that dist value to the current know distnace to the neighbor
                    if distance_through_min_dist_node < distances[neighbor]:
                        # Update the value for distances dict
                        distances[neighbor] = distance_through_min_dist_node
                        # Update the value for the predecessors dict 
                        predecessors[neighbor] = min_dist_node
    return []


def get_min_dist_node(distances, unvisited):
    min_dist = float("inf")
    node_label = None

    if not unvisited:
        return None
    # Iterate through unvisited set
    for node in unvisited:
        # Set variable for the distance value from the distances dict key 
        distance = distances[node]
        # If distance is less then current min distance
        if distance < min_dist:
            # Update min_dist value to distance
            min_dist = distance
            # Update node_label to be current min_distance node
            node_label = node
    # Return the value of node_label or the node with the smallest distance
    return node_label


def get_path(dest, predecessors):
    final_path = []
    current_pos = dest
    # Continue while loop as long as there is a predecessor for current_pos
    while predecessors.get(current_pos):
        # Add current_pos to final_path list
        final_path.append(current_pos)
        # Update current_pos to the predecessor of the current_pos
        current_pos = predecessors.get(current_pos)
    # Add the final pos to the list
    final_path.append(current_pos)
    # Reverse the list once constructed to ensure correct order
    final_path.reverse()
    return final_path




### Greedy Algorithms
'''
Dijkstra's algorithm is a greedy algorithm. Greedy algorithms make short-sighted optimization choices, and as such are good at finding local maximums. If the local maximum isn't also the global maximum, then greedy algorithms can result in sub-optimal solutions.

When it comes to the kind of graph traversal we've been doing, the local maximum is guaranteed to be the global maximum, so Dijkstra's can guarantee the shortest path.

Local maximums
Greedy algorithms are bad when the solution space has many local maximums:

Local Maximum

No local maximums
Greedy algorithms are great when the local maximum is the global maximum
'''


### BELLMAN FORD ALGORITHM

# Big-O Notation is O(V*E)

'''
The Bellman Ford algorithm computes shortest paths from a single node to all other nodes in a weighted graph. You may be thinking

Why can't I just use Dijkstra's algorithm for that?

You can, and you should because it's a bit faster. The problem is Dijkstra's algorithm can't handle negative weights in the graph. If there are negative weights, you'll need to use something different like Bellman-Ford.

The Bellman-Ford algorithm consists of two phases.

Relaxation Phase: This phase consists of N-1 iterations, where N is equal to the number of vertices in the graph. During each iteration the edges are "relaxed", meaning it updates the shortest path estimate for each edge. If there are no negative cycles the distance from the source to all vertices is guaranteed to be correct.

Negative Cycle Detection Phase: A final iteration is done to check whether any distances are reduced further. If any distance can still be reduced there must be a negative weight cycle in the graph.

To summarize: not only does the Bellman-Ford algorithm handle negative weights, but it properly detects and reports negative cycles.
'''


def bellman_ford(graph, src, dest):
    # Initialize the distances dictionary to store the shortest path estimates
    distances = {}

    # Set the initial distances: 0 for the source node and infinity for all others
    for node in graph:
        if node == src:
            distances[node] = 0  # Source node starts with a distance of 0
        else:
            distances[node] = float("inf")  # All other nodes start with "infinity"

    # Perform relaxation for (number of nodes - 1) times
    for _ in range(len(graph) - 1):
        # Iterate over all nodes
        for node in graph:
            # Check each neighbor of the node
            for neighbor in graph[node]: 
                # Get the weight of the edge from node to neighbor
                weight = graph[node][neighbor]
                # If a shorter path to neighbor is found, update the distance
                if distances[node] != float("inf") and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Perform one additional iteration to check for negative weight cycles
    for node in graph:
        for neighbor in graph[node]:
            weight = graph[node][neighbor]
            # If we find a shorter path, there's a negative cycle
            if distances[node] != float("inf") and distances[node] + weight < distances[neighbor]:
                raise Exception("Negative cycle detected!")  # Raise an error if a negative cycle is detected

    # Return the shortest path to the destination node
    return distances[dest]

'''
Key Aspects of the Algorithm:
Initialization: Allows you to track the minimum cost from the source node to each other node.
Relaxation Loop: Repeatedly updates shortest paths for all nodes and edges, ensuring you discover the shortest possible paths.
Negative Cycle Check: Ensures that no further improvements can be made after completing len(graph) - 1 relaxations unless there's a cycle with a net negative cost.
'''


'''
Why len(graph) - 1 Relaxations?
Path Lengths:

In a graph with N nodes, the longest possible simple path between any two nodes involves N-1 edges. This is because once you've added an Nth edge, 
you must be revisiting a node and thus creating a cycle.

Relaxation Process:

Each relaxation step ensures that known paths from the source are minimized as much as possible.
After N-1 iterations, any simple path from the source will have been fully relaxed. In other words, 
the shortest path to any node will have been found because the algorithm has had the opportunity to examine every possible path length.
Negative Cycle Detection:

Further relaxation beyond N-1 iterations should not result in any shorter paths unless there's a negative weight cycle. 
That's why the Bellman-Ford algorithm performs one additional relaxation round to detect such cycles.
Example:
Consider a simple graph:

A --1--> B --1--> C --1--> D
Copy icon
With 4 nodes (A, B, C, D), N = 4.
The longest simple path in this graph is 3 edges long (e.g., A to B to C to D).
Thus, to ensure the shortest path for all nodes is discovered, we relax the edges N-1 = 3 times.
This way, the Bellman-Ford is guaranteed to discover the shortest paths without getting trapped by infinitely reducing paths in the event of a negative cycle. 
It leverages the longest path constraint as a logical step to ensure completeness. 
Hope this answers your query clearly!
'''



### Priority Queues

'''
A priority queue is a data structure similar to a regular queue but where each element additionally has a priority associated with it. In our priority queue, an element with low priority is served before an element with high priority, though this can go either way.

In some implementations, if two elements have the same priority, they are served according to the order in which they were enqueued, while in other implementations, the ordering of elements with the same priority is undefined.

Priority queues can have insert and pop methods that are Big O(log(n)). These kinds of fast priority queues can speed up algorithms like Dijkstra's.
'''

class PriorityQueue:
    def __init__(self):
        # Initialize an empty list to store elements as tuples of (priority, item)
        self.elements = []

    def empty(self):
        # Check if the queue is empty by verifying if 'elements' has any items
        return len(self.elements) == 0

    def push(self, priority, item):
        # Add a new tuple of (priority, item) to the end of the queue
        self.elements.append((priority, item))

    def pop(self):
        # If the queue is empty, return None to indicate there's no item to pop
        if self.empty():
            return None
        # Initialize 'min' to track the index of the tuple with the smallest priority
        min = 0
        # Iterate through elements to find the tuple with the lowest priority
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        # Remove and store the tuple with the lowest priority
        item = self.elements[min]
        # Delete the tuple from the elements list
        del self.elements[min]
        # Return the item associated with the lowest priority
        return item[1]
    

# HEAPS 

'''
A heap data structure is optimized for retrieving the largest or smallest element in a collection. In the case of a max heap (largest element) 
it's a balanced tree where the value of each node is always greater than or equal to the value of its children.
The root node is always the largest or smallest element in the tree, which means finding the min or max, depending on the type of heap, is a blazingly fast operation.

A heap where the root node is the smallest element is called a min heap
A heap where the root node is the largest element is called a max heap
Min Heap Visualization
A list can be used to represent the heap, which may seem tricky, but by doing some math with the indexes in the list, we can keep track of the tree structure.
'''



### MIN HEAP CLASS


class MinHeap:
    def pop(self):
        if len(self.elements) == 0:
            return None

        root_value = self.elements[0]

        if len(self.elements) == 1:
            self.elements.pop()
            return root_value

        self.elements[0] = self.elements.pop()
        self.bubble_down(0)

        return root_value


    def bubble_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        min_index = index

        if (
            left_child_index < len(self.elements)
            and self.elements[left_child_index][0] < self.elements[min_index][0]
        ):
            min_index = left_child_index

        if (
            right_child_index < len(self.elements)
            and self.elements[right_child_index][0] < self.elements[min_index][0]
        ):
            min_index = right_child_index

        if min_index != index:
            self.elements[index], self.elements[min_index] = (
                self.elements[min_index],
                self.elements[index],
            )
            self.bubble_down(min_index)


    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)


    def bubble_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.elements[index][0] < self.elements[parent][0]:
            self.elements[index], self.elements[parent] = self.elements[parent], self.elements[index]
            self.bubble_up(parent)


    def __init__(self):
        self.elements = []


    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0][1]
    

'''
Why Use Heaps?
Heaps are fast because they are designed to be hyper-efficient for one simple task: finding the minimum or maximum element in a collection. We don't need to be able to search them, or even index into them. We just need to quickly find the minimum or maximum element and maintain that order as we add and remove elements.

Big O Analysis
insert(): O(log(n)). We need to do one operation per "level" of the tree, that is, once for each parent of the node being inserted.
peek(): O(1). We just need to look at the root node.

'''


###Priority Queue with a Heap
'''
As you probably noticed, the API for our PriorityQueue class is very similar to the API for our Heap class. In fact, a heap is essentially a priority queue where the priority is the value of the node.

Remember that our original naive implementation of a priority queue was just a list. It had the following Big O complexities:

peek: O(1)
push: O(n)
pop: O(n)
Once we upgraded to a min heap, we got the following complexities:

peek: O(1)
push: O(log(n))
pop: O(log(n))
The difference between O(log(n)) and O(n) is huge! It can be the difference between 1,000,000 operations taking 1 second as opposed to ~14 hours.
'''

import random


class TrafficGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, tile):
        return (
            tile.x >= 0 and tile.x < self.width
            and tile.y >= 0 and tile.y < self.height
        )

    def neighbors(self, tile):
        adjacent_tiles = []
        
        east_tile = Tile(tile.x + 1, tile.y)
        west_tile = Tile(tile.x - 1, tile.y)
        south_tile = Tile(tile.x, tile.y - 1)
        north_tile = Tile(tile.x, tile.y + 1)
        
        adjacent_tiles.extend([east_tile, west_tile, south_tile, north_tile])

        filtered = filter(self.in_bounds, adjacent_tiles)

        return list(filtered)

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        return random.randint(1, 25)

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
    

### A* Search Algorithm

# We built the TrafficGrid and the PriorityQueue so that we can use them in our implementation of the A* search algorithm.

'''Why use A*? (pronounced a-star)
The A* Search algorithm is one of the best and most popular techniques used in path-finding.

A* algorithms, unlike other traversal techniques like Dijkstra's and Bellman-Ford, has "brains". A* is a "smart" algorithm It differentiates itself from other conventional algorithms through the use of heuristics.

What is a heuristic?
Heuristics in computer science and artificial intelligence are “rules of thumb” used in algorithms to assist in finding faster solutions to complex problems.

With a good heuristic, A* can still guarantee 100% accuracy, but a bad heuristic can result in a suboptimal solution.
'''


'''A* algorithm or A-star algorithm'''
'''
1. Create a new empty PriorityQueue()
2. Push the src tile onto the queue with a priority of 0
3. Create a dictionary of Tile->PredecessorTile. Set src's predecessor to None to start. Keep in mind that we can use Tile objects as keys in sets and dictionaries because we provided a __hash__ method.
4. Create a dictionary of Tile->int called costs. Set src's cost to 0 to start.
5. Create a new empty set() called visited that will hold all the Tiles the algorithm has visited so far
6. While the queue isn't empty:
    1. Pop the next Tile off the priority queue, this will be the lowest cost tile to move to
    2. If the next tile is the destination, break out of the while loop
    3. If the next tile is in the visited set continue to the next iteration of the while loop
    4. Add the next tile to visited.
    5. For each of the next tile's neighbors:
        1. Calculate the total cost to the neighbor by adding the value in the costs dictionary for the current Tile to the neighbor's cost()
        2. If the neighbor doesn't yet have a cost in the costs dictionary or its total cost is less than its previously known cost:
            1. Set the known cost for the neighbor to the newly calculated total cost
            2. Calculate the priority of the neighbor by adding the total cost to its heuristic()
            3. Push the neighbor into the priority queue using the priority
            4. Add the neighbor to the predecessors dictionary pointing to the Tile we just came from
7. When the while loop exits, we'll have found the best path, now we need to extract the path from the predecessors dictionary. Create an empty list called path.
8. Create a variable called pred and set it equal to the destination
9. While pred isn't None:
    1. Append pred to the path
    2. Set pred to it's predecessor
10. Reverse the path and return it
'''

''' The heuristic functions purpose and how it makes A* a faster algorithm then Dijkstra's algorithm
The Manhattan distance provides a lower bound, or the minimum number of steps required to reach the destination, assuming no obstacles block the direct path.

If your actual path cost is equal to the heuristic (Manhattan distance): It means you are taking the most efficient path possible, closely following the minimum estimate.
If the actual path cost is greater than the heuristic: This indicates that your path must navigate around obstacles, making it longer than the direct path.
If your actual path cost is somehow less than the heuristic: This would imply something illogical in a typical grid setup, as the Manhattan distance represents the minimal direct path on an unobstructed grid.
Therefore, the heuristic helps the algorithm make informed decisions, guiding it to explore paths that are likely more promising and dismiss those that appear unnecessarily lengthy.
'''

import random


def heuristic(next, dest):
    dist_formula = abs(next.x - dest.x) + abs(next.y - dest.y)
    return dist_formula

def a_star_search(muddy_grid, src, dest):
    queue = PriorityQueue()
    queue.push(0, src)
    predecessors = {
        src: None
    }
    costs = {
        src: 0
    }
    visited = set()

    while not queue.empty():
        current = queue.pop()
        if current == dest:
            break
        if current in visited:
            continue
        visited.add(current)
        for next in muddy_grid.neighbors(current):
            next_cost_so_far = costs[current] + next.cost()
            if next not in costs or next_cost_so_far < costs[next]:
                costs[next] = next_cost_so_far
                priority = next_cost_so_far + heuristic(next, dest)
                queue.push(priority, next)
                predecessors[next] = current

    path = []
    pred = dest
    while pred != None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self):
        random.seed(hash(self))
        bucket = random.randint(1, 2)
        cost = random.randint(1, 5)
        if bucket == 2:
            cost = random.randint(15, 20)
        return cost

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        else:
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TrafficGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, tile):
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def neighbors(self, tile):
        neighbors = [
            Tile(tile.x + 1, tile.y),
            Tile(tile.x - 1, tile.y),
            Tile(tile.x, tile.y - 1),
            Tile(tile.x, tile.y + 1),
        ]
        results = filter(self.in_bounds, neighbors)
        return results

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost():02d}]"
            s += "\n"
        return s
    

# Intro to Dynamic Programming

'''
Dynamic Programming is an optimization technique. Wherever we see a solution to a problem that has repeated iterations for the same inputs, we can optimize it using Dynamic Programming.
The idea is to simply remember the results of subproblems, so that we don't have to re-compute them. This can save our algorithms immense amounts of time.

Problems need to have two properties in order to be improved using dynamic programming:

Overlapping subproblems
An optimal substructure
'''

# Overlapping subproblems

'''
The core concept behind dynamic programming is to divide a problem into sub-problems and save the result for the future so that we will not have to compute that same problem again. 
Assuming there are some subproblems that repeat, we can save a lot of time by using the cached result.
'''

### Fast Fibonacci Memoization

def fibonacci(n, precomputed={}):
    if n not in precomputed:
        if n == 0:
            precomputed[n] = 0
        elif n == 1:
            precomputed[n] = 1
        else:
            precomputed[n] = fibonacci(
                n-1, precomputed) + fibonacci(n-2, precomputed)
    return precomputed[n]


# Memoization

'''
Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.
'''

# Memoization VS Caching

'''
Memoization is a specific type of caching. While caching can refer generally to any storing technique like web page caching, memoizing specifically involves caching the return values of a function for algorithmic use.
'''

# Tradeoffs

'''
Memoization is a way to lower a function's time cost in exchange for space cost. In most cases, this means trading memory (RAM) for compute resources (CPU). 
Memoized functions become optimized for speed in exchange for a higher use of computer memory space.
'''

# Tabulation VS Memoization

'''
Memoization is considered a "top down" optimization. It's top-down because we start with the whole problem and then move down into the subproblems (via recursive function calls).

Tabulation takes the opposite approach, that's why it's referred to as a "bottom up" method. Tabulation involves solving all the subproblems first, then assembling them into the final solution.
'''

# Implementing Tabulation for Fibonacci sequence 

def fibonacci(n):
    # Use list comprehension to create a list with n+1 entries with each entry being None
    fib_results = [None for _ in range(n+1)]
    # Set the first entry to 0
    fib_results[0] = 0
    # If n is greater than 0, set the second entry to 1
    if n > 0:
        fib_results[1] = 1
    # For each number at i index from 2 to n inclusive 
    for i in range(2, len(fib_results)):
        # Set i to the sum of item i-1 and i-2
        fib_results[i] = (
            fib_results[i - 1] + fib_results[i - 2]
        )
    # Return the item at index n
    return fib_results[n]



# Slow Edit distance 

def edit_distance(str1, str2):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    else:
        insert = edit_distance(str1, str2[:-1])
        remove = edit_distance(str1[:-1], str2)
        substitute = edit_distance(str1[:-1], str2[:-1])
    return 1 + min(insert, remove, substitute)


# Dynamic Programming edit distance


def edit_distance(str1, str2):
   table = []
   for _ in range(0, len(str1)+1):
      row = []
      for _ in range(0, len(str2)+1):
         row.append(0)
      table.append(row)

   for i in range(0, len(table)):
      for j in range(0, len(table[i])):
         # First string is empty
         # Distance is length of second string
         if i == 0:
               table[i][j] = j

         # Second string is empty
         # Distance is length of first string
         elif j == 0:
               table[i][j] = i

         # Last characters are same
         # Distance is the same as strict substrings
         elif str1[i-1] == str2[j-1]:
               table[i][j] = table[i-1][j-1]

         # If last character are different, consider all
         # possibilities and find minimum
         else:
               table[i][j] = 1 + min(
                  table[i][j-1],   # Insert
                  table[i-1][j],   # Remove
                  table[i-1][j-1]  # Replace
               )
   return table[-1][-1]


'''
--Tabulation (Bottom-Up):

We solve all subproblems first and use those to construct a solution for the main problem.
Implemented using iteration and typically with a table (like an array).
Think: "Fill out the table completely before getting the final answer."


--Memoization (Top-Down):

We solve the main problem and recursively break it into subproblems, caching results to avoid redundant calculations.
Implemented using recursion and caching/store mechanisms like dictionaries.
Think: "Solve the main problem and recall the solution to subproblems as needed."
'''


### Linear Programming Intro
'''
Linear programming is a technique where we depict complex relationships through linear functions and then find the optimum inputs to maximize for a given output. The real relationships might be much more complex – but we can simplify them to linear relationships.

In LP we're given some variables, and we want to assign real values to them in order to:

Satisfy a related set of linear equations and/or linear inequalities
Maximize or minimize a given linear function'''


'''
A linear programs can be represented in a Tableau, which is just a fancy word for a matrix.

The Tableau is useful because it allows us to keep track of the state of the program (moving around the vertices of the graph) without storing all the vertices explicitly.
'''

# Objective function
# profit = x * 5 + y

# or

# -5x - y + profit = 0

# Constraints
# x <= 250
# y <= 200
# x + y <= 300
# 0 <= x
# 0 <= y

# self.constraints: [250, 200, 300]

# Tableau:
# self.rows = [1.0, 0.0]
#             [0.0, 1.0]
#             [1.0, 1.0]
# self.objective =  [-5.0, -1.0]


'''
Baseline: You're absolutely correct that this gives us a baseline. In the simplex method, we start at the origin (where all variables are zero) and move towards the optimal solution.

Consistency: By having all variables on one side and zero on the other, we create a consistent format for all equations in our system (objective function and constraints). 
This consistency makes it easier to apply the algorithm systematically.

Improvement direction: The negative coefficients in the objective function row of the tableau actually help indicate which direction we should move to improve our solution. 
If we see a negative value in the bottom row (excluding the rightmost column), it suggests that increasing that variable will improve our objective function value.

Stopping condition: This format also gives us a clear stopping condition. When all values in the bottom row (except the rightmost) are non-negative, we've reached the optimal solution.

Pivot selection: The arrangement helps in selecting pivot elements during the algorithm's iterations, guiding us towards the optimal solution step by step.
'''

# The Tableau is basically just a matrix of coefficients, which really makes it a system of equations. The nice thing about systems of equations is we can do mathematical operations on them, 
# and because we know they share variables, one equation can provide information about another.

# -5x - y + profit = 0
# 1x  + 0y          <= 250
# 0x  + 1y          <= 200
# 1x  + 1y          <= 300


# Slack Variables

'''
For each inequality constraint, we need to add a new variable, called a slack variable. The purpose of the slack variable is to change the inequality constraint to an equality constraint. 
This variable represents the difference between the two sides of the inequality and is assumed to be non-negative. For example, the inequalities
'''

# 1x + 0y <= 250
# 0x + 1y <= 200
# 1x + 1y <= 300

# become

# 1x + 0y + s1 = 250
# 0x + 1y + s2 = 200
# 1x + 1y + s3 = 300


# By adding a slack variable for each inequality, the size of our tableau will grow, because instead of two variables, x and y, we now have 5 variables, x, y, s1, s2, and s3.


class SimplexSolver:
    def solve(self):
        self.add_slack_variables()
        while self.should_pivot():
            pivot_col = self.get_pivot_col()
            pivot_row = self.get_pivot_row(pivot_col)
            self.pivot(pivot_row, pivot_col)
            

    # don't touch below this line

    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def get_pivot_col(self):
        low = 0
        pivot_idx = 0
        for i in range(len(self.objective) - 1):
            if self.objective[i] < low:
                low = self.objective[i]
                pivot_idx = i
        return pivot_idx

    def get_pivot_row(self, col_idx):
        last_col = [self.rows[i][-1] for i in range(len(self.rows))]
        pivot_col = [self.rows[i][col_idx] for i in range(len(self.rows))]
        min_ratio = float("inf")
        min_ratio_idx = -1
        for i in range(len(last_col)):
            ratio = float("inf")
            if pivot_col[i] == 0:
                ratio = 99999999
            else:
                ratio = last_col[i] / pivot_col[i]
            if ratio < 0:
                continue
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_idx = i
        if min_ratio_idx == -1:
            raise Exception("no non-negative ratios, problem doesn't have a solution")
        return min_ratio_idx

    def pivot(self, pivot_row_idx, pivot_col_idx):
        pivot_val = self.rows[pivot_row_idx][pivot_col_idx]
        for i in range(len(self.rows[pivot_row_idx])):
            self.rows[pivot_row_idx][i] = self.rows[pivot_row_idx][i] / pivot_val
        for i in range(len(self.rows)):
            if i == pivot_row_idx:
                continue
            mul = self.rows[i][pivot_col_idx]
            for j in range(len(self.rows[i])):
                self.rows[i][j] = self.rows[i][j] - mul * self.rows[pivot_row_idx][j]
        mul = self.objective[pivot_col_idx]
        for i in range(len(self.objective)):
            self.objective[i] = self.objective[i] - mul * self.rows[pivot_row_idx][i]

    def should_pivot(self):
        return min(self.objective[:-1]) < 0

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)

    def get_solution_from_tableau(self):
        cols = []
        for colI in range(len(self.rows[0])):
            col = [0] * len(self.rows)
            for rowI in range(len(self.rows)):
                col[rowI] = self.rows[rowI][colI]
            cols.append(col)

        results = []
        for i in range(len(cols) - 1):
            if cols[i].count(0) == len(cols[i]) - 1 and 1 in cols[i]:
                results.append(cols[-1][cols[i].index(1)])
            else:
                results.append(0)
        return results, self.objective[-1]

    


'''
Simplex Tableau - Basic Variables and the solution
Basic and non-basic variables
-5x - y + profit = 0
1x  + 0y          <= 250
0x  + 1y          <= 200
1x  + 1y          <= 300

became

  x    y   s1   s2   s3   constraint
[1.0, 0.0, 1.0, 0.0, 0.0, 250.0]
[0.0, 1.0, 0.0, 1.0, 0.0, 200.0]
[1.0, 1.0, 0.0, 0.0, 1.0, 300.0]
[-5.0, -1.0, 0.0, 0.0, 0.0, 0.0]

The tableau is useful due to it's two kinds of variables, basic and non-basic variables. In the tableau's current initial state, all the slack variables, s1, s2, and s3 are basic. x and y are non-basic.

In a Simplex tableau, a variable is basic if its the only number you see in its column and that number is exactly 1.

Who cares about basic variables?
To any dictionary there's an associated solution to the system of equations: just set all the non-basic variables to zero and compute the values of the basic variables. For the tableau above the associated solution is:

x = 0
y = 0
s1 = 250
s2 = 200
s3 = 300

As you can probably tell, this isn't the optimal solution to our problem. This is just the initial state of the tableau, and as you can see, it represents the point (0,0) on our graph, 
which is just the starting point, not the final vertex.
'''

