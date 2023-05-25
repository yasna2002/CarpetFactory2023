import numpy as np

import Design
import Navigation
import Search

if __name__ == '__main__':
    print(".-. Welcome To CARPET FACTORY .-.\n")
    print("1.Design a new carpet")
    print("2.Search a carpet")
    print("3.Buy a carpet")
    print("4.Finding the nearest factory store")

    option = int(input("Enter 1 to 4: "))

    if option == 1:  # ....................................................................... option 1

        print("\n----------------------------Design a new carpet----------------------------")

        map_of_carpet = dict()
        n = int(input("number of areas : "))
        print("enter areas related to each other with the following format :"
              " a b c ... \na : main vertex")
        for i in range(n):  # creating map_of_carpet dict
            vertex_list = input().split()
            key = vertex_list.pop(0)
            map_of_carpet[key] = vertex_list

        colored_areas = (Design.color_carpet(map_of_carpet))  # a dict of colored areas

        max_color = 0
        for i in colored_areas.values():  # finding maximum color needed to color the carpet
            if i > max_color:
                max_color = i
        print("Maximum color needed to color the carpet : ", max_color + 1)
        print(colored_areas)

    if option == 2:  # ....................................................................... option 2

        print("\n----------------------------Search a carpet----------------------------")

        matrix1 = np.random.randint(0, 5, size=(300, 400))
        matrix2 = np.random.randint(0, 5, size=(300, 400))

        print(matrix1)
        print(matrix2)

        percentage = Search.matrix_match_percentage(matrix1, matrix2)

        print(f"Percentage match: {percentage}%")

    if option == 4:  # ....................................................................... option 4

        print("\n----------------------------Finding the nearest factory store----------------------------")

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
            distance, path = Navigation.dijkstra(intersections, start, intersection)
            distances.append(distance)
            paths.append(path)
        min_distance = min(distances)
        print("Minimum distance :", min_distance)
        branch = branches[paths[distances.index(min_distance)][-1]]
        print("You can go to branch", branch, "in", paths[distances.index(min_distance)][-1], "intersection")
        print("Here is the path :", *paths[distances.index(min_distance)])