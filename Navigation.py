import heapq


def dijkstra(intersections, start, end):

    distances = {node: float('inf') for node in intersections}
    distances[start] = 0

    pre = {node: None for node in intersections}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in intersections[current_node].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                pre[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    path = []
    current_node = end

    while current_node:
        path.append(current_node)
        current_node = pre[current_node]

    path.reverse()

    return distances[end], path


if __name__ == '__main__':

    intersections = {
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

    branches = {
        'Vokala': 1,
        'Emam': 2,
        'Azadi': 3
    }

    start = input("Your location : ")
    distances = []
    paths = []

    for intersection in branches.keys():
        distance, path = dijkstra(intersections, start, intersection)
        distances.append(distance)
        paths.append(path)
    min_distance = min(distances)
    print("Minimum distance :", min_distance)
    branch = branches[paths[distances.index(min_distance)][-1]]
    print("You can go to branch", branch, "in", paths[distances.index(min_distance)][-1], "intersection")
    print("Here is the path :", *paths[distances.index(min_distance)])
