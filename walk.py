routes = []
weight = []
a = []


def pathRenew(node, cities, path, distance,weight):

    path.append(node)
    print("node append" + str(path))

    if len(path) > 1:
        a = [item for item in weight if node in item]
        a = [item for item in a if path[-2] in item]

        distance += a[0][2]
        print("distance renewed" + str(distance))

    if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
        global routes
        path.append(path[0])
        a = [item for item in weight if node in item]
        a = [item for item in a if path[0] in item]

        distance += a[0][2]

        print(str(path) + "" + str(distance))
        routes.append([distance, path])
        return

    for city in cities:
        if (city not in path) and (node in cities[city]):
            pathRenew(city, dict(cities), list(path), distance,weight)

def shortpath(msg):
    routes.sort()

    if len(routes) != 0:
        msg.setWindowTitle("TOTAL: "+str(len(routes))+" Routes Available")
        if len(routes)>10:

            text = "Total routes exceed 10 thus we show first 10"
            first10route =[]
            for i in range(0,10):
                first10route.append(routes[i])
            print("TOTAL: " + str(len(routes)) + " Routes Available")
            print("Shortest route:" + str(routes[0]) + "\n" + "Other routes: " + str(routes))
            msg.setText("Shortest route:" + str(routes[0]) + "\n" + text+ " Other routes: " + str(first10route))
            msg.exec_()

        else:
            print("TOTAL: "+str(len(routes))+" Routes Available")
            print("Shortest route:" + str(routes[0]) + "\n" + "Other routes: " + str(routes))
            msg.setText("Shortest route:" + str(routes[0]) + "\n" + " Other routes: " + str(routes))
            msg.exec_()
        return routes
    else:
        print("FAIL!")






