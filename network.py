import numpy as np
import math
import pandas

import string_gen



class Node:
	def __init__(self, name, x, y, graph):
		self.x = x
		self.y = y
		self.name = name
		self.connections = set()
		graph.addNode(self)

	def __str__(self):
		return self.name

	def addConnection(self, edge):
		self.connections.add(edge)

class Edge:
	def __init__(self, node1, node2, weight, graph):
		self.ends = {node1, node2}
		self.name = '{' + str(node1) + ', ' + str(node2) + '}'
		self.weight = weight
		for i in self.ends:
			i.addConnection(self)
		graph.addEdge(self)

	def __str__(self):
		return self.name


class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = set()

	def addNode(self, node):
		self.nodes.add(node)

	def addEdge(self, edge):
		self.edges.add(edge)

	def printGraph(self):
		for i in self.nodes:
			print i

	def getNearestNeighbor(self, confirmedList):
		minimum = 100
		edgeList = set()
		tentative = None
		for node in confirmedList.keys():
			for edge in node.connections:
				for end in edge.ends:
					if end not in confirmedList.keys():
						edgeList.add(edge)
		for i in edgeList:
			if i.weight < minimum:
				tentative = i
		for node in tentative.ends:
			if node not in confirmedList.keys():
				return node, tentative.weight
		


	def findPath(self, start, end):
		confirmedMin = {start: 0}
		tentativeMin = None
		while end not in confirmedMin.keys():
			j = confirmedMin.keys()
			node, weight = self.getNearestNeighbor(confirmedMin)
			confirmedMin[node] = weight
		for i in confirmedMin.keys():
			print(str(i) + ": " + str(confirmedMin[i]))

id_list = string_gen.id_generator(size = 100)
x_list = np.random.random_integers(5, size = 100)
y_list = np.random.random_integers(5, size = 100)
G = Graph()
A = Node('A', 0, 0, G)
inputs = zip(id_list, x_list, y_list, [G]*100)
for i in inputs:
	B = Node(i[0], i[1], i[2], G)
	AB = Edge(A, B, 1, G)
	print(AB)
