"""
description: An implementation of a vertex as part of a graph.
file: labE_graph.py
language: python3
Author: Sean Strout @ RIT CS

Code taken from the online textbook and modified:
http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""
class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (movie name)
    """
    __slots__ = 'id','connectedTo'

    def __init__(self, key):
         self.id = key
         self.connectedTo = {}

    def addNeighbor(self, nbr, weight=""):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight : The edge cost(movie name)
        :return: None
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:
            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        # Modified to include edge name(movie name)
        return str(self.id) + ' connectedTo: ' + str([str(x.id) + "("+str(self.getWeight(x))+")" for x in self.connectedTo])

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight
        """
        return self.connectedTo[nbr]
