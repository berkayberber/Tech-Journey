import time
import datetime
import astar
import data_pre_processing
import djikstra


def main():
    start_stop = "Renoma"
    start_time = "10:00:00"
    end_stop = "PL. GRUNWALDZKI"

    graph = data_pre_processing.create_graph('connection_graph.csv')
    ends = astar.get_nodes_by_name(graph, end_stop, start_time)
    start = astar.get_start_node(graph, start_stop, start_time, ends[0])

    print("start searching")


    # A* (combined cost)
    start_time = time.time()
    path_astar, cost_astar = astar.astar(start, ends, astar.cost_combined, astar.geo_distance)
    end_time = time.time()
    # Convert start_time and end_time to human-readable format
    start_time_readable = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time_readable = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("------------------------ astar combined")
    print(
        f"From {start_stop} To {end_stop} at {start_time_readable} by {end_time_readable} in {cost_astar} minutes by:")
    for node in path_astar:
        print(node)


    # A* (time cost)
    start_time = time.time()
    path_astar, cost_astar = astar.astar(start, ends, astar.cost_time, astar.geo_distance)
    end_time = time.time()
    # Convert start_time and end_time to human-readable format
    start_time_readable = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time_readable = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("------------------------ astar time")
    print(
        f"From {start_stop} To {end_stop} at {start_time_readable} by {end_time_readable} in {cost_astar} minutes by:")
    for node in path_astar:
        print(node)


    # A* line cost
    start_time = time.time()
    path_astar, cost_astar = astar.astar(start, ends, astar.cost_switch_line, astar.geo_distance)
    end_time = time.time()
    # Convert start_time and end_time to human-readable format
    start_time_readable = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time_readable = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("------------------------ astra line")
    print(
        f"From {start_stop} To {end_stop} at {start_time_readable} by {end_time_readable} in {cost_astar} minutes by:")
    for node in path_astar:
        print(node)

    # Dijkstra (combined cost)
    start_time = time.time()
    path_dijkstra, cost_dijkstra = djikstra.dijkstra(graph, start, ends, astar.cost_combined)
    end_time = time.time()
    # Convert start_time and end_time to human-readable format
    start_time_readable = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time_readable = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("------------------------ djikstra combined")
    print(
        f"From {start_stop} To {end_stop} at {start_time_readable} by {end_time_readable} in {cost_dijkstra} minutes by:")
    for node in path_dijkstra:
        print(node)


    # Dijkstra (time cost)
    start_time = time.time()
    path_dijkstra, cost_dijkstra = djikstra.dijkstra(graph, start, ends, astar.cost_time)
    end_time = time.time()
    # Convert start_time and end_time to human-readable format
    start_time_readable = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time_readable = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("------------------------djikstra time")
    print(
        f"From {start_stop} To {end_stop} at {start_time_readable} by {end_time_readable} in {cost_dijkstra} minutes by:")
    for node in path_dijkstra:
        print(node)

    # Dijkstra (line cost)
    start_time = time.time()
    path_dijkstra, cost_dijkstra = djikstra.dijkstra(graph, start, ends, astar.cost_switch_line)
    end_time = time.time()
    # Convert start_time and end_time to human-readable format
    start_time_readable = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time_readable = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print("------------------------djikstra line")
    print(
        f"From {start_stop} To {end_stop} at {start_time_readable} by {end_time_readable} in {cost_dijkstra} minutes by:")
    for node in path_dijkstra:
        print(node)


    # run the algorithms and measure the time taken for each
    start_time = time.time()
    path_astar_combined, cost_astar_combined = astar.astar(start, ends, astar.cost_combined, astar.geo_distance)
    time_astar_combined = time.time() - start_time

    start_time = time.time()
    path_astar_time, cost_astar_time = astar.astar(start, ends, astar.cost_time, astar.geo_distance)
    time_astar_time = time.time() - start_time

    start_time = time.time()
    path_astar_line, cost_astar_line = astar.astar(start, ends, astar.cost_switch_line, astar.geo_distance)
    time_astar_line = time.time() - start_time

    start_time = time.time()
    path_dijkstra_combined, cost_dijkstra_combined = djikstra.dijkstra(graph, start, ends, astar.cost_combined)
    time_dijkstra_combined = time.time() - start_time

    start_time = time.time()
    path_dijkstra_time, cost_dijkstra_time = djikstra.dijkstra(graph, start, ends, astar.cost_time)
    time_dijkstra_time = time.time() - start_time

    start_time = time.time()
    path_dijkstra_line, cost_dijkstra_line = djikstra.dijkstra(graph, start, ends, astar.cost_switch_line)
    time_dijkstra_line = time.time() - start_time

    print("Time taken by each algorithm:")
    print(" ")
    print(f"A* (combined cost): {time_astar_combined} seconds")
    print(f"A* (time cost): {time_astar_time} seconds")
    print(f"A* (line cost): {time_astar_line} seconds")
    print(f"Dijkstra (combined cost): {time_dijkstra_combined} seconds")
    print(f"Dijkstra (time cost): {time_dijkstra_time} seconds")
    print(f"Dijkstra (line cost): {time_dijkstra_line} seconds")





if __name__ == "__main__":
    main()