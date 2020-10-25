from GraphDj import *

def Djikstra():
    print("Алгоритм Декстры")
    start = int(root[1].attrib['start.id'])
    goal = int(root[1].attrib['goal.id'])
    path = []
    open = [start]
    closed = []
    while len(open) != 0:
        objects = []
        for i in range(len(open)):
            j = open[i]
            objects.append(nodes[j-1])
        open = []
        objects.sort()
        for i in range(len(objects)):
            open.append(objects[i].id)
        current = open[0]
        open.pop(0)
        closed.append(current)
        for i in range(len(edges)):
            if edges[i].source == current:
                if current == goal:
                    print("OPEN = ", open)
                    print("CLOSED = ", closed)
                    value = nodes[current - 1].g
                    print("Стоимость пути = ", value)
                    node = current
                    path.append(current)
                    while node != start:
                        path.append(nodes[node-1].parent)
                        node = nodes[node-1].parent
                    path.reverse()
                    return path
                neighbour = edges[i].target
                if neighbour in closed:
                    continue
                if nodes[neighbour - 1].g > nodes[current - 1].g + edges[i].weight:
                    nodes[neighbour - 1].g = nodes[current - 1].g + edges[i].weight
                    nodes[neighbour - 1].parent = current
                if neighbour in open:
                    continue
                open.append(neighbour)
    return "Path not found"
