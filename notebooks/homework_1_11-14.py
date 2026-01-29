import networkx as nx
from src.plotting_utilities import show_graph, show_degree_distribution

#G = nx.complete_graph(8)
#G = nx.circulant_graph(8,[1]) 
#G = nx.circulant_graph(8,[1,2])
G = nx.barbell_graph(3,2)
show_graph(G)

show_degree_distribution(G)
