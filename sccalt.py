##Simon Gelber - CSC359 Asgn 2
# Identify Strongly Connected Components
import sys
from collections import defaultdict

class Graph:

    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.pre = []

        self.post = []

        self.disc = []
        # No. of vertices
        self.numV = 0

        self.clock = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def previsit(self, v):
        self.pre[v] = self.clock
        self.clock += 1

    def postvisit(self, v):
        self.post[v] = self.clock
        self.clock += 1

    def explore(self, v):
        self.disc[v] = True
        self.previsit(v)
        for u in self.graph[v]:
            if self.disc[u] is False:
                self.explore(u)
        self.postvisit(v)


    def scc(self):

        for x in range(self.numV):
            if self.disc[x] is False:
                self.explore(x)

        print(self.graph)
        print(self.pre)
        print(self.post)
        for i in range(self.numV):
            for neighbor in self.graph[i]:
                if self.pre[neighbor] < self.pre[i] and self.post[neighbor] > self.post[i]:






def main(argv):
    G = Graph()
    file = open(argv[1],"r")
    edges = file.readline()
    while edges:
        edges = edges.strip()
        numberslist = edges.split(", ")
        G.add_edge(int(numberslist[0]),int(numberslist[1]))
        if int(numberslist[1]) not in G.graph:
            G.graph[int(numberslist[1])] = []
        G.graph[int(numberslist[0])].sort()
        edges = file.readline()
    #singleValue = scc()
    G.numV = len(G.graph)
    G.disc = [False] * G.numV
    G.pre = [-1] * G.numV
    G.post = [-1] * G.numV
    G.scc()
    #print(G.pre)
    #print(G.post)
    #print(G.numV)
    #print(G.graph)
    #print(G.disc)
    file.close()



if __name__ == "__main__":
    main(sys.argv)