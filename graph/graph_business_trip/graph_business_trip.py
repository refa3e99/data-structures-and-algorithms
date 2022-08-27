def business_trip(graph, cities_array):
    """
    Given a graph and a list of cities_array.
    :param graph:
    :param cities_array:
    :return: the cost for going from city to another city
    """
    cost = 0
    if len(cities_array) == 0:
        return None
    for city in range(len(cities_array) - 1):
        for neighbor in graph.get_neighbors(cities_array[city]):
            if neighbor.vertex == cities_array[city + 1]:
                cost += neighbor.weight

    if cost == 0:
        return None
    else:
        return cost