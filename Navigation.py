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
