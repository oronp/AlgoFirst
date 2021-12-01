import random


def question1(graph, size):
    # Prim's Algorithm in Python

    MST = graphBuilder(size)
    INF = 9999999
    selected_node = [0] * size
    no_edge = 0
    selected_node[0] = True

    while no_edge < size - 1:

        minimum = INF
        a = 0
        b = 0
        for m in range(size):
            if selected_node[m]:
                for n in range(size):
                    if (not selected_node[n]) and graph[m][n]:
                        # not in selected and there is an edge
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n
        # print(str(a) + "-" + str(b) + ":" + str(graph[a][b]))
        MST[a][b] = graph[a][b]
        selected_node[b] = True
        no_edge += 1
    return MST


def randomTable(graph, size):
    for i in range(size):
        for j in range(size):
            graph[i][j] = random.randint(0, 100)
    for i in range(size):
        graph[i][i] = 0
    return graph


def graphBuilder(size):
    table = []

    for r in range(size):
        row = []
        for c in range(size):
            row.append(0)
        table.append(row)
    return table


def bowBuilder(graph, size):
    while True:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if x != y:
            if graph[x][y] == 0:
                newBow = [x, y, random.randint(0, 100)]
                break
    return newBow


def question2(graph, size, newBow):
    graph[newBow[0]][newBow[1]] = newBow[2]
    i = 0
    count = 0

    while True:

        if graph[i][newBow[1]] > newBow[2]:
            if i == 0:
                for r in range(size):
                    if graph[0][r] == 0:
                        count += 1
                if count == (size - 1):
                    graph[newBow[0]][newBow[1]] = 0
                    break
            graph[i][newBow[1]] = 0
            break
        elif graph[i][newBow[1]] <= newBow[2] and graph[i][newBow[1]] != 0:
            graph[newBow[0]][newBow[1]] = 0
            break
        elif graph[i][newBow[1]] == 0:
            i += 1

    return graph


def graphPrinter(graph, size):
    for i in range(size):
        print("[", end=""),
        for j in range(size):
            if j == size-1:
                print(str(graph[i][j]), end="")
            else:
                print(str(graph[i][j]) + ",", end=""),
        print("]"),
    print(
        "_________________________________________________________________________________________")



#####################################################################
# number of vertices in graph
SizeOfGraph = random.randint(20, 30)
# creating graph by adjacency matrix method
G = randomTable(graphBuilder(SizeOfGraph), SizeOfGraph)

print("This is the first graph:")
graphPrinter(G, SizeOfGraph)
# print(G)

print("This is the MST graph:")
graphPrinter(question1(G, SizeOfGraph),SizeOfGraph)

MST = question1(G, SizeOfGraph)
newBow1 = bowBuilder(MST, SizeOfGraph)

print("This is the new vertex:")
print(newBow1)
print("_________________________________________________________________________________________")
print("This is the new MST graph, after we added the new vertex:")

graphPrinter(question2(MST, SizeOfGraph, newBow1),SizeOfGraph)
