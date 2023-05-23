distances = []
pathes = []


def printSolution(dist, end, distance_result):
    """""
    print(dist[end])
    print(*distance_result)
    """""
    distances.append(dist[end])
    pathes.append(distance_result)


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist, sptSet):

        min = 1e7

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, start, end, cities):

        dist = [1e7] * self.V
        dist[start] = 0
        sptSet = [False] * self.V
        distance_result = []

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
            distance_result.append(cities[u])
            if u == end:
                break

        printSolution(dist, end, distance_result)


if __name__ == '__main__':

    number_of_intersections = 15
    g = Graph(number_of_intersections)

    intersections = ["Vokala", "Freiburg", "Azadi", "Enghelab", "Shariati", "Taleghani", "Afarinesh",
                     "Valiasr", "Emam", "Jomhori", "Shohada", "Takhti", "Daneshgah", "Bahonar", "Baharestan"]

    number_of_streets = 24

    streets = [["Vokala", "Freiburg", "300"], ["Vokala", "Enghelab", "200"], ["Vokala", "Valiasr", "100"],
               ["Freiburg", "Azadi", "400"], ["Azadi", "Shariati", "250"], ["Freiburg", "Shariati", "350"],
               ["Freiburg", "Taleghani", "280"], ["Taleghani", "Valiasr", "330"], ["Valiasr", "Emam", "360"],
               ["Valiasr", "Jomhori", "500"], ["Emam", "Jomhori", "450"], ["Emam", "Baharestan", "900"],
               ["Jomhori", "Baharestan", "800"], ["Bahonar", "Baharestan", "700"], ["Bahonar", "Daneshgah", "300"],
               ["Bahonar", "Takhti", "400"], ["Bahonar", "Jomhori", "650"], ["Takhti", "Daneshgah", "250"],
               ["Takhti", "Shohada", "500"], ["Daneshgah", "Shohada", "200"], ["Taleghani", "Shohada", "950"],
               ["Afarinesh", "Shohada", "400"], ["Shariati", "Afarinesh", "150"], ["Enghelab", "Taleghani", "250"]]

    number_of_branches = 5
    branches = {
        1: "Vokala",
        2: "Shohada",
        3: "Taleghani",
        4: "Emam",
        5: "Azadi"
    }

    start = input("Your location : ")

    g.graph = []
    for city in intersections:
        list = []
        for i in range(number_of_intersections):
            list.append(0)
        for i in range(number_of_streets):
            if city == streets[i][0]:
                index = intersections.index(streets[i][1])
                list[index] = int(streets[i][2])
            elif city == streets[i][1]:
                index = intersections.index(streets[i][0])
                list[index] = int(streets[i][2])

        g.graph.append(list)

    for intersection in branches.values():
        g.dijkstra(intersections.index(start), intersections.index(intersection), intersections)
    min_distance = min(distances)
    print(min_distance)
    print(*pathes[distances.index(min_distance)])
