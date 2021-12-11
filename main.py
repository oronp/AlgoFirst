#Nir varsanno 216727489
#Idan Zafrani 316061100


import random

def question1(graph, size):
    # Prim's Algorithm in Python

    MST = graphBuilder(size)
    INF = 9999999
    selected_node = [0] * size
    selected_node[0] = True
    no_edge = 0
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
        MST[b][a] = graph[a][b]
        selected_node[b] = True
        no_edge += 1
    return MST


def randomTable(graph, size):
    for i in range(size):
        for j in range(size):
            x = random.randint(0,100)
            graph[i][j] = x;
            graph[j][i] = x;
            # graph[i][j] = random.randint(0, 100)
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
                newBow = [x, y, random.randint(1, 3)]
                break
    return newBow


def question2(graph, size, newBow):

    maxNum = 999999
    nodes = [0] * size
    graph[newBow[0]][newBow[1]] = newBow[2]
    graph[newBow[1]][newBow[0]] = newBow[2]
    graphPrinter(graph,size)
    path1 = DFS2D(graph,size,newBow[0],newBow[1])
    path2 = DFS2D(graph,size,newBow[1],newBow[0])
    finalPath = []
    for element in path1:
        if element in path2:
            finalPath.append(element)
    print(finalPath)
    while finalPath:
        i = finalPath.pop()
        for j in range(size):



# אנחנו עוברים רק על השורות שמופיעות ב״דרך״ ובשורות הללו נמצא את המספר המקסימלי (נעבור רק על החצי העליון הימני של המטריצה כדי לחסוך יעילות)
#כל הזכויות שמורות לעידן ואורון ואמן שאלון וניר יידרסו על ידי קורקינט חשמלי שזה מוות משפיל אחושרמוטה (אמן שהקורקינט יהיה רום שירכיב את מנשרי והוא יעשה לניר פייפר קאט כי הוא וקטור)

def DFS2D(graph,size,startPoint,endPoint):
    stack = []
    path = []
    access = False
    stack.append(startPoint)
    while stack:
        current = stack.pop()
        if current in path:
            continue
        path.append(current)
        if access and graph[current][endPoint] != 0:
            path.append(endPoint)
            return path
        for neighbor in range(size):
            if graph[current][neighbor] != 0 and neighbor != endPoint:
                stack.append(neighbor)

        access = True
    return path

# לא להכניס את הנקודת סיום על ההתניה הראשונה
# אם הכנסו את הנקודת סיום אז אנחנו יוצאים ומחזירים את הדרך הנוכחית


def graphPrinter(graph, size):
    for i in range(size):
        print("[", end=""),
        for j in range(size):
            if j == size-1:
                print(str(graph[i][j]), end="")
            else:
                print(str(graph[i][j]) + " , ", end=""),
        print("]"),
    print(
        "_________________________________________________________________________________________")


#####################################################################
# number of vertices in graph
SizeOfGraph = random.randint(4, 5)
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

question2(MST,SizeOfGraph,newBow1)

# graphPrinter(question2(MST, SizeOfGraph, newBow1),SizeOfGraph)