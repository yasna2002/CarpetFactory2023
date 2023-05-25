def color_carpet(areas):
    vertices = sorted((list(areas.keys())))
    colour_graph = {}

    for vertex in vertices:
        unused_colours = len(vertices) * [True]

        for neighbor in areas[vertex]:
            if neighbor in colour_graph:
                colour = colour_graph[neighbor]
                unused_colours[colour] = False
        for colour, unused in enumerate(unused_colours):
            if unused:
                colour_graph[vertex] = colour
                break

    return colour_graph


if __name__ == '__main__':

    map_of_carpet = dict()
    n = int(input("number of areas : "))
    print("enter areas related to each other with the following format :"
          " a b c ... \na : main vertex")
    for i in range(n): # creating map_of_carpet dict
        vertex_list = input().split()
        key = vertex_list.pop(0)
        map_of_carpet[key] = vertex_list

    colored_areas = (color_carpet(map_of_carpet)) # a dict of colored areas

    max_color = 0
    for i in colored_areas.values(): # finding maximum color needed to color the carpet
        if i > max_color:
            max_color = i
    print("Maximum color needed to color the carpet : ", max_color + 1)
    print(colored_areas)
