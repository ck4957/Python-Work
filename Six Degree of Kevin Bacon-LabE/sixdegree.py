"""
description: An implementation of a Six dergee of Kevin Bacon using graph data structure
file: labE_graph.py
language: python3
Author: Chirag Kular
"""

from labE_graph import *

# Global Constant
THREE_LINKS = 4  # If there are 3 movie links, then number of actors will be plus 1.

def createGraph(file):
    """
    Builds the Graph by reading the data line by line from the file instance
    :param file:instance of the input file
    :return:object of created graph
    """
    g = Graph()

    for line in file:
        line = line.strip()
        biglist = line.split()
        movie_name = biglist[0]
        # List to store the actor's first names and Last name as one value
        actor_names = []
        for i in range(1, len(biglist), 2):
            actor_names.append(biglist[i]+" "+biglist[i+1])

        # Traversing the list using two for loops to create edges from the first
        # actor with remaining actors in the same list & storing the movie name as edge
        for i in range(0, len(actor_names)-1):
            for j in range(i+1, len(actor_names)):
                g.addEdge(actor_names[i], actor_names[j], movie_name)
                g.addEdge(actor_names[j], actor_names[i], movie_name)
    return g


def printGraph(g):
    """
    Print all the vertices in the graph with their
    :param g:instance of the created graph
    :return:
    """
    print("--------------------------------------------------------")
    print("Vertices and their connections in graph are as follows: ")
    for vertices in g:
        print(vertices)
    print("--------------------------------------------------------")

def findpath(g):
    """
    This function prompts the user for two vertices i.e start and end
    Then this values are passed as argument to findshortestpath function
    which returns the shortest path if exists
    :param g: instance of the created graph
    :return:
    """
    start = input("Enter starting node name :")
    if g.getVertex(start) is None:
        print("Starting Node is not present in the graph ")
        return None
    else:
        start = g.getVertex(start)

    end = input("Enter goal node name :")
    if g.getVertex(end) is None:
        print("Goal Node is not present in the graph ")
        return None
    else:
        end = g.getVertex(end)

    print("------------------------------------------------------")
    path = findShortestPath(start, end)
    #print(len(path))
    if path is None or len(path) > THREE_LINKS or len(path) is 1:
        print("No chain exists")
    else:
        for i in range(len(path)):
            print(path[i].id)
            if i+1 < len(path):
                print("\twas in "+path[i].getWeight(path[i+1])+" with")


def main():
    """
    Prompts the user for the file name and invokes the create graph,
    which returns the graph instance and that instance is passed as an argument
    in printGraph and findpath functions
    :return:
    """
    try:
        file_name = input("Enter the File name :")
        file = open(file_name)
        sixdegree_graph = createGraph(file)
        printGraph(sixdegree_graph)
        findpath(sixdegree_graph)
    except FileNotFoundError:
        print("File not Found")


if __name__ == '__main__':
    main()