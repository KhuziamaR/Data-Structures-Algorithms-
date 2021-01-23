# BFS is good for finding shortest paths or closer nodes
# BFS REQUIRES MORE MEMORY

# DFS uses Less memory, Does path exist? 
# DFS is slower


# //////////////////////////// BREADTH FIRST SEARCH 
# The Algorithm
#   1)   Pick any node, visit the adjacent unvisited vertex, 
#        mark it as visited, display it, and insert it in a queue.
#   2)   If there are no remaining adjacent vertices left, remove the first vertex from the queue.
#   3)    Repeat step 1 and step 2 until the queue is empty or the desired node is found.