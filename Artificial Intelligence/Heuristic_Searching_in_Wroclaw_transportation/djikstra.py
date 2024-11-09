import heapq
import astar
import data_pre_processing


def dijkstra(graph, start, end, cost_fn):
    distances = {node: float('inf') for node in graph} # initialize the all nodes with infinity.
    distances[start] = 0

    previous_nodes = {node: None for node in graph}
    #smallest value is highest priority.
    priority_queue = [(0, start)] # each tuple contains curr distance to a node and not itself.
# enters loop till priority_queue is mpty
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) # pop alwas retrieves the unvisited node with smallest distance. once it popped itmarked as visited'
        # pops the nodoe with smallest distance from priority_queue. so become curr node

# checks if the current node is goal.
# Repeatedly selecting the unvisited node with the smallest known distance
        if current_node in end:
            path = []  # store nodes in found path.
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]  # previous_nodes dict stores the parent of each node along the shortest path. move one-step backward.
            path.reverse()
            return path, current_distance  # goal nodes are returned

# for each neighbor of curr node calculated tentative_distance by..   tentative allowes compare the new potential node with previously known best.
        for neighbor in graph[current_node]:
            tentative_distance = current_distance + cost_fn(current_node, neighbor) # potential tentaive distance to reach the neighbor through path
# if tentative is smaller than the previously recorded distance to the neighbor, update the neighbor distance.
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance  # if small then update recorded shortest distance to neighbor
                previous_nodes[neighbor] = current_node  #store curr node as the parent of neighbor.
                heapq.heappush(priority_queue, (tentative_distance, neighbor)) # add the neighbor and ts updated distance
# add the neighbor along with its new tentative_distance to priority queue.
# keep the nodes ordered by thir distance values.
    return None, None  # none if we dnot reached the end
