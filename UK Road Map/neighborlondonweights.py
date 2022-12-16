from graph import City, load_graph
import networkx as nx

nodes, graph = load_graph("roadmap.dot", City.from_dict)

for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)