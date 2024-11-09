from datetime import datetime,time
import pprint
from dataclasses import dataclass # used for representation of data and its storage.
import pandas as pd  # data manipulation and analysis


@dataclass
class RideInformation:
    line: str
    departure_time: datetime.time
    arrival_time: datetime.time
    start_stop: str
    end_stop: str

@dataclass
class GeoInformation:
    start_lat: float
    start_long: float
    stop_lat: float
    stop_lon: float
#fund b
class Node:
    # constructor: initializes new node object  with the ride,geo info and neighbours.
    def __init__(self, ride_info: RideInformation, geo_info: GeoInformation):
        self.ride_info = ride_info
        self.geo_info = geo_info
        self.neighbours = []  # list that stores references to neighboring nodes in the graph. represents other stops that can be reached directly from curr node.

#  override the default string representation of a Node.
    def __str__(self):
        return f"Node {self.ride_info.line} start {self.ride_info.start_stop} {self.ride_info.departure_time}" \
               f" end {self.ride_info.end_stop} {self.ride_info.arrival_time}"
# define comparison for two node objects based on dep_time. used in algort pri que
    def __lt__(self, other):
        return self if self.ride_info.departure_time < other.ride_info.departure_time else other
    # for setting the neighbor nodes for the curr node.
    # the condition compares d_time of each potential neighbor node with arr_time of curr node.
    def set_neighbours(self, nodes_by_start_stop: dict):
        try:
            self.neighbours = list(filter(lambda node: (node.ride_info.departure_time >= self.ride_info.arrival_time), nodes_by_start_stop[self.ride_info.end_stop]))
        except KeyError:
            self.neighbours = []

def create_graph(filename: str):  # string that represents the path to the csv file which contains the data
    graph = {}  # empty dictionary to store graph representation.
  # reads data from the CSV file pandas DataFrame 'df'. and specifying datatpes of each column using 'dtype' parameter.
    df = pd.read_csv(filename,
                     dtype={"unnamed": int, "company": str, "line": str, "departure_time": str, "arrival_time": str
                         , "start_stop": str, "end_stop": str, "start_stop_lat": float, "start_stop_lon": float,
                            "end_stop_lat": float, "end_stop_lon": float})
    nodes_list = []  # empty list to store all nodes in graph.

    node_by_start_stop_dict = {}
    # These variables initialized to keep track of number of nodes created and number of neighbours added.
    nodes_created = 0
    neighbours_added=0

    for index, row in df.iterrows():  # Iterate over each row of the df using df.iterrows().

        ride_info = RideInformation(
            row['line'],
            parse_time(row['departure_time']),
            parse_time(row['arrival_time']),
            row['start_stop'],
            row['end_stop'])
        geo_info = GeoInformation(
            float(row['start_stop_lat']),
            float(row['start_stop_lon']),
            float(row['end_stop_lat']),
            float(row['end_stop_lon']),
        )
        n = Node(ride_info, geo_info)  # Create node object using extracted info.
    # check if there is already a node associated with start stop of the current node.
        if (start_stop := n.ride_info.start_stop) not in node_by_start_stop_dict:
            node_by_start_stop_dict[start_stop] = [n]
        else:
            node_by_start_stop_dict[start_stop].append(n)

        nodes_list.append(n)
        nodes_created += 1  # increment the counter

    for node in nodes_list:
        neighbours_added += 1

        node.set_neighbours(node_by_start_stop_dict)
        graph[node] = node.neighbours
    return graph

# used to convert a str representation of time into a time. -> HH:MM:SS 'datetime'
def parse_time(t: str):
    h, m, s = int(t[0:2]), int(t[3:5]), int(t[6:8])
    return time(h, m, s)






