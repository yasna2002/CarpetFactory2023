import heapq

distances = []
pathes = []


def dijkstra(graph, source, destination):
    # Create a dictionary to store the distance from the source to each node
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Create a dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph}

    # Create a priority queue to store nodes and their tentative distances
    priority_queue = [(0, source)]

    while priority_queue:
        # Pop the node with the smallest tentative distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Stop if we reach the destination
        if current_node == destination:
            break

        # Skip if the current distance is greater than the stored distance
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Build the shortest path from source to destination
    path = []
    current_node = destination

    while current_node:
        path.append(current_node)
        current_node = previous[current_node]

    path.reverse()

    return distances[destination], path


if __name__ == '__main__':

    number_of_intersections = 15

    intersections = ["Vokala", "Freiburg", "Azadi", "Enghelab", "Shariati", "Taleghani", "Afarinesh",
                     "Valiasr", "Emam", "Jomhori", "Shohada", "Takhti", "Daneshgah", "Bahonar", "Baharestan"]

    number_of_streets = 24

    graph = {
        'Vokala': {'Freiburg': 300, 'Enghelab': 200, 'Valiasr': 100},
        'Freiburg': {'Vokala': 300, 'Azadi': 400, 'Shariati': 350, 'Taleghani': 280},
        'Azadi': {'Freiburg': 400, 'Shariati': 250, 'Valiasr': 100},
        'Enghelab': {'Vokala': 200, 'Taleghani': 250},
        'Shariati': {'Azadi': 250, 'Freiburg': 350, 'Afarinesh': 150},
        'Taleghani': {'Freiburg': 280, 'Valiasr': 330, 'Shohada': 950},
        'Afarinesh': {'Shohada': 400, 'Shariati': 150},
        'Valiasr': {'Vokala': 100, 'Taleghani': 330, 'Emam': 360, 'Jomhori': 500},
        'Emam': {'Valiasr': 360, 'Jomhori': 450, 'Baharestan': 900},
        'Jomhori': {'Valiasr': 500, 'Emam': 450, 'Baharestan': 800, 'Bahonar': 650},
        'Shohada': {'Takhti': 500, 'Daneshgah': 200, 'Taleghani': 950, 'Afarinesh': 400},
        'Takhti': {'Daneshgah': 250, 'Bahonar': 400, 'Shohada': 500},
        'Daneshgah': {'Bahonar': 300, 'Takhti': 250, 'Shohada': 200},
        'Bahonar': {'Baharestan': 700, 'Daneshgah': 300, 'Jomhori': 650, 'Takhti': 400},
        'Baharestan': {'Emam': 900, 'Jomhori': 800, 'Bahonar': 700}
    }

    number_of_branches = 5
    branches = {
        'Vokala': 1,
        'Emam': 2,
        'Azadi': 3
    }

    start = input("Your location : ")

    for intersection in branches.keys():
        distance, path = dijkstra(graph, start, intersection)
        distances.append(distance)
        pathes.append(path)
    min_distance = min(distances)
    print("Minimum distance :", min_distance)
    branch = branches[pathes[distances.index(min_distance)][-1]]
    print("You can go to branch", branch, "in", pathes[distances.index(min_distance)][-1], "intersection")
    print("Here is the path :", *pathes[distances.index(min_distance)])
