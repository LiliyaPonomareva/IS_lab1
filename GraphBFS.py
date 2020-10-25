import xml.etree.ElementTree as ET

tree = ET.parse('graph_example.xml')
root = tree.getroot()


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Node:
    def __init__(self, id, g, parent):
        self.id = id
        self.g = g
        self.parent = parent


nodes = []
edges = []
for i in range(len(root[2])):
    if 'source' in root[2][i].attrib:
        source = int(root[2][i].attrib['source'])
        target = int(root[2][i].attrib['target'])
        weight = int(root[2][i].attrib['weight'])
        edge1 = Edge(source, target, weight)
        edges.append(edge1)
    if 'id' in root[2][i].attrib:
        id = int(root[2][i].attrib['id'])
        g = 0
        parent = 0
        node1 = Node(id, g, parent)
        nodes.append(node1)