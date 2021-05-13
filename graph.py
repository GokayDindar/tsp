import itertools
import random
import string
import math

class Graph:

    def __init__(self,no_nodes=None):

        self.no_nodes = 0
        self.no_edges = 0
        self.nodes = []
        self.nodes1 = {}
        self.coordinatesX = [0]
        self.coordinatesY = [0]
        self.graphList = {}
        self.adj = {}
        self.edges = []
        self.edges_weights=[]

        self.no_nodes = no_nodes
        self.no_edges = random.randint(self.no_nodes+1,((self.no_nodes*(self.no_nodes-1))/2)-1) + 1

        self.createGraph()


    def randNodeName(self):
        buffer = list(string.ascii_lowercase)[random.randint(0, 25)] + list(string.ascii_uppercase)[
                random.randint(0, 25)] + str(random.randint(0, 90))

        while buffer in self.nodes1.keys():
            buffer = list(string.ascii_lowercase)[random.randint(0, 25)] + list(string.ascii_uppercase)[
                random.randint(0, 25)] + str(random.randint(0, 90))
        return buffer

    def createGraph(self):
        print("create called")
        overflowProtection = 1000000

        while len(self.nodes1.keys())<self.no_nodes:
            circle = {
                "name":self.randNodeName(),
                "x":random.randint(30,1800),
                "y": random.randint(30,900),
                "adj":list(self.nodes1.keys()),
                "weights":[]
            }
            overlapping = False

            for j in self.nodes1:
                dist = math.dist([circle["x"],circle["y"]],[self.nodes1[j][0],self.nodes1[j][1]])
                if dist < 50:
                    overlapping = True
                    print("CALCULATING")
                    break
            if not overlapping:
                w = []
                for a in range(0, len(self.nodes1.keys())):
                    w.append(random.randint(0,10))
                self.nodes1[circle["name"]]=[circle["x"],circle["y"],circle["adj"]]
                self.nodes.append(circle["name"])
                #self.graphList[circle["name"]] =  circle["adj"]
                w.clear()

            else:
                overflowProtection += -1

            if overflowProtection == 0:
                print("OVERFLOW REACHED MTH")
                #print("NUMBER OF NODES ON SCREEN: " + str(len(self.nodes1.keys())))
                break
        self.edges = list((itertools.product(self.nodes, repeat=2))) # we did product for not exceed the total edge number
        self.edges = list(set(tuple(sorted(t)) for t in self.edges))

        #print("edges without dup filt:  " + str(self.edges))
        for a in reversed(self.edges):
            if a[0] == a[1] or a[1] == a[0]:
                print("duplicated tuple element ="+ str(a[0]) +"\t"+ str(a[1]))
                self.edges.remove(a)

        self.edges = random.sample(self.edges, self.no_edges)
        print("edges:  " + str(self.edges))

        edgesAllVariant = self.edges.copy()
        for e in self.edges:
            edgesAllVariant.append((e[1],e[0]))
        print(str(edgesAllVariant))
        self.adj = {k: [v[1] for v in g] for k, g in itertools.groupby(sorted(edgesAllVariant), lambda e: e[0])}
        for i in range(0,len(self.edges)):
            self.edges_weights.append(self.edges[i]+(random.randint(1,10),))
        print("weight" + str(self.edges_weights))
        print("adj_Dict:  " + str(self.adj))
        #print("nodes:  " + str(self.nodes1))






