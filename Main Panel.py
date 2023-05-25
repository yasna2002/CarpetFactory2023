import numpy as np

import Design
import Navigation
import Search
from selling import most_carpet

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

        print("The carpet you want to search is : \n")
        entry_carpet = np.random.randint(1, 4, size=(300, 400))
        print(entry_carpet)
        list_of_carpets = Search.carpet_maker()

        list_of_percentages = []
        for carpet in list_of_carpets:  # obtaining matching percentage
            list_of_percentages.append(Search.carpet_match_percentage(entry_carpet, carpet))

        sorted_percentages = Search.quicksort_high_to_low(list_of_percentages)
        for i in range(1, 4):  # printing top 3 matched carpets
            index_of_carpet = list_of_percentages.index(sorted_percentages[i])
            print("\nmatching carpet", i, "with", "%.3f" % sorted_percentages[i], "% match:\n\n",
                  list_of_carpets[index_of_carpet])

    if option == 3:  # ....................................................................... option 3

        print("\n----------------------------Buy a Carpet----------------------------")

        carpets = [600, 300, 300, 500, 600, 400, 250, 150, 450]
        print("Your Budget: ")
        customer_money = int(input())
        n = len(carpets)
        most_carpet(customer_money, carpets, n)

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