from GraphBFS import *

def BFS():
    print("Поиск в ширину")
    start = int(root[1].attrib['start.id'])
    goal = int(root[1].attrib['goal.id'])
    path = []
    open = [start]
    closed = []
    while len(open) != 0:
        current = open[0]
        open.pop(0)
        closed.append(current)
        for i in range(len(edges)):
            if edges[i].source == current:
                neighbour = edges[i].target
                if (neighbour in open) or (neighbour in closed):
                    continue
                nodes[neighbour - 1].g = nodes[current - 1].g + 1
                nodes[neighbour - 1].parent = current
                open.append(neighbour)
                if neighbour == goal:
                    print("OPEN = ", open)
                    print("CLOSED = ", closed)
                    value = nodes[neighbour - 1].g
                    print("Стоимость пути = ", value)
                    node = neighbour
                    path.append(neighbour)
                    while node != start:
                        path.append(nodes[node-1].parent)
                        node = nodes[node-1].parent
                    path.reverse()
                    return path
    return "Path not found"

