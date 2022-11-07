##Simon Gelber - CSC359 Asgn 2
# Identify Strongly Connected Components
import sys
from collections import defaultdict

class Graph:

    def __init__(self):
        #Dictionary to store graph
        self.graph = defaultdict(list)

        #Number of vertices
        self.numV = 0


    def add_edge(self, v, u):
        self.graph[v].append(u)


    def explore(self, v, stack, disc):
        disc[v] = True

        for u in self.graph[v]:
            if disc[u] is False:
                self.explore(u, stack, disc)
        stack.append(v)


    def reverse_graph(self):
        new_graph = Graph()
        new_graph.numV = self.numV

        for v in self.graph:
            for u in self.graph[v]:
                new_graph.add_edge(u,v)
        return new_graph


    def output_scc(self, v, disc, output, numscc):
        disc[v] = True
        output[numscc].append(v)

        for u in self.graph[v]:
            if disc[u] is False:
                self.output_scc(u, disc, output, numscc)

    def scc(self):

        stack = []
        disc = [False] * self.numV
        output = defaultdict(list)
        numscc = 0
        firstnum = 0
        for x in range(self.numV):
            if disc[x] is False:
                self.explore(x, stack, disc)

        rev_graph = self.reverse_graph()
        disc = [False]*self.numV

        while stack:
            vert = stack.pop()
            if disc[vert] is False:
                rev_graph.output_scc(vert, disc, output, numscc)
                output[numscc].sort()
                numscc += 1
        print(str(len(output)) + " Strongly Connected Component(s):")
        for key in sorted(output, key = lambda k:output[k][0], reverse=False):
            for nums in output[key]:
                if firstnum == 0:
                    print(nums, end="")
                    firstnum += 1
                else:
                    print(", ", end="")
                    print(nums, end="")
            print("")
            firstnum = 0


def main(argv):
    G = Graph()
    file = open(argv[1],"r")
    numVert = 0
    edges = file.readline()
    while edges:
        edges = edges.strip()
        numberslist = edges.split(", ")
        G.add_edge(int(numberslist[0]),int(numberslist[1]))
        if int(numberslist[0]) > numVert:
            numVert = int(numberslist[0])
        elif int(numberslist[1]) > numVert:
            numVert = int(numberslist[1])
        G.graph[int(numberslist[0])].sort()
        edges = file.readline()
    G.numV = numVert + 1
    G.scc()
    file.close()



if __name__ == "__main__":
    main(sys.argv)