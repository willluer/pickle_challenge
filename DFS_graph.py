def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

letter_map = {"0":[],\
              "1":[],\
              "2":["A","B","C"],\
              "3":["D","E"],\
              "4":["G","H","I"],\
              "5":["J","K","L"],\
              "6":["M","N"],\
              "7":["P","Q","R","S"],\
              "8":["T","U","V"],\
              "9":["W","X","Y","Z"]}

def construct_graph(digits):
    graph = {}
    prev_node = letter_map[digits[0]] # [D,E,F]
    graph["$"] = set(prev_node)
    for i in range(len(digits)):
        for letter in prev_node:
            graph[letter] = set(letter_map[digits[i]])
        prev_node = letter_map[digits[i]]
    print(graph)
    return graph

# list(dfs_paths(construct_graph(), 'A', 'F'))



path = dfs(construct_graph("363"), "3")
print(path)
