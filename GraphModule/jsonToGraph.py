import json
import GraphModule as g


def jsonToGraph(json_file):
    json_data = open(json_file)
    json_object = json.load(json_data)
    json_data.close
    graph = g.Graph()

    for description in json_object.keys():
        for data in json_object[description]:
            if description == 'vertex':
                vertex = g.Vertex(data['id'])
                graph.addVertex(vertex)
            if description == "edge":
                startVertex = g.Vertex(data['start'])
                endVertex = g.Vertex(data['end'])
                edge = g.Edge(startVertex, endVertex, data['weight'])
                graph.addEdge(edge, data['undirected'])

    return graph
