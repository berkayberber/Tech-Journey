import heapq
import math
from datetime import datetime, date, time
from typing import List, Callable

import geopy.distance

import data_pre_processing
from data_pre_processing import Node


def astar(start: Node, goal: List[Node], cost_fn: Callable[[Node, Node], int],
          heuristic_fn: Callable[[Node, Node], float]):
    front = [(0, start)]  # priority queue(heap) contains nodes to be evaluated. exlplore nodes
    came_from = {start: None}
    cost_so_far = {start: 0}  # Dictionary to store the cost of reaching each neighbor from the start node

    end_node = None
    # loop that continues until the priority queue front is empty. algorithm continues till it reaches the goal node.
    # pop the node with the lowest cost from priority queue and assigned to current.
    while front:
        _, current = heapq.heappop(front)

  # algorithm runs until the priority queue goal node is reached
        if current in goal:
            end_node = current
            break

        for neighbor in current.neighbours:
            new_cost = cost_so_far[current] + cost_fn(current, neighbor)  # sums the cost to reach the curr node from start node and the cost from the curr node to its neighbor.
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:  # check if neighbor node not visited or if the new cost to reach the neighbor is less than the previous cost.
                cost_so_far[neighbor] = new_cost  # If new cost is lower, updates the cost recorded for reaching neighbor node.
                g_n = new_cost
                h_n = heuristic_fn(goal[0], neighbor)  # assume only one goal node and curr neighbor node.
                priority = g_n + h_n
                heapq.heappush(front, (priority, neighbor))
                came_from[neighbor] = current # after adding the neighbor node to the priority queue,
 # ensure srat node to the end node b following the parents stored in came_from dict.

    # representation of the shortest path found from the starting point to the goal. actual sequence.
    path = []
    current = end_node
    while current != start:
        path.append(current)
        current = came_from[current] # update
    path.append(start)
    path.reverse()

    return path, cost_so_far[end_node] # computed path and associated cost from the start node to the end node.

# to find starting node based on a given starting stop name, starting time and target node.
# determines the earliest departure time from that stop occurring after 20:00:00.
def get_start_node(graph: dict, start_dest: str, start_time: str, end_node: Node):
    start_time = data_pre_processing.parse_time(start_time)
    earliest_start_node = None
    for node in graph.keys():
        if node.ride_info.start_stop == start_dest and node.ride_info.departure_time > start_time:
            if earliest_start_node is None:
                earliest_start_node = node
            elif node.ride_info.departure_time < earliest_start_node.ride_info.departure_time and \
                    geo_distance(earliest_start_node, end_node) >= geo_distance(node, end_node):
                print(f'{earliest_start_node},   {node}')
                earliest_start_node = node
    return earliest_start_node  # the node with the earliest departure time is returned.

# to retrieve nodes from a graph based on certain criteria. find all nodes named and filter before 20
def get_nodes_by_name(graph: dict, stop: str, time: str): # destination stp, target arrive time
    candidates = [] # to store nodes that meets the specified criteria.
    time = data_pre_processing.parse_time(time)
    for node in graph.keys():
        if node.ride_info.end_stop == stop and node.ride_info.arrival_time > time: # checks if the node's ride info (destination stop) matches the specified stop and if the arrival time of the node is after the target arrival time (time)
            candidates.append(node)
    return candidates

# calculates the heuristic val based on the geographic distance between curr node and end node.
def geo_distance(a: Node, b: Node) -> float:
    return geopy.distance.geodesic((a.geo_info.start_lat, a.geo_info.start_long),
                                   (b.geo_info.start_lat, b.geo_info.start_long)).km

# time cost between two nodes. Computes the time difference between the dep time of node a and the dep_time of the node b.
def cost_time(a: Node, b: Node):
    return int((datetime.combine(date.min, b.ride_info.departure_time) -
                datetime.combine(date.min, a.ride_info.departure_time)).total_seconds() // 60)

# cost associated switching lines between nodes.
def cost_switch_line(a: Node, b: Node):
    if a.ride_info.line != b.ride_info.line or a.ride_info.arrival_time != b.ride_info.departure_time:
        return 5
    return 0
# If the lines of the two nodes are different or if the arrival time of node a is not equal to the departure time of node b, a fixed cost of 5 is returned. Otherwise, the cost is 0, indicating no penalty for switching lines.

# combines the time cost and switch line cost between nodes a,b.
def cost_combined(a, b):
    return cost_time(a, b) + cost_switch_line(a, b) * 2
