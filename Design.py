def colour_vertices(areas):
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

    areas = dict()
    n = int(input("number of areas : "))
    print("enter areas related to each other with the following format :"
          " a b c ... \na : main vertex")
    for i in range(n):
        vertex_list = input().split()
        key = vertex_list.pop(0)
        areas[key] = vertex_list

    colored_carpet = (colour_vertices(areas))

    max = 0
    for i in colored_carpet.values():
        if i > max:
            max = i
    print("Maximum color needed to color the carpet : ", max + 1)
    print(colored_carpet)
