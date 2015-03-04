from collections import deque
import pprint
import numpy as np


class Hopcroft_Karp():
    INF = np.inf

    def __init__(self, Adj):
        self.Adj = Adj
        self.U, self.V = self.bipartite_sets()
        self.G = self.U.union(self.V)
        self.pair = {}
        self.dist = {}
        for v in self.G:
            self.pair[v] = None
            self.dist[v] = self.INF

    def bipartite_sets(self):
        U = set()
        V = set()
        for from_node, to_nodes in self.Adj.iteritems():
            if set(to_nodes).intersection(U) == set():
                U.add(from_node)
            else:
                V.add(from_node)
        return U, V

    def bfs(self):
        d = deque()
        for v in self.U:
            if self.pair[v] == None:
                self.dist[v] = 0
                d.append(v)
            else:
                self.dist[v] = self.INF
        self.dist[None] = self.INF
        while len(d) > 0:
            v = d.popleft()
            if self.dist[v] < self.dist[None]:
                for u in self.Adj[v]:
                    if self.dist[self.pair[u]] == self.INF:
                        self.dist[self.pair[u]] = self.dist[v] + 1
        return self.dist[None] != self.INF

    def dfs(self, v):
        if v is not None:
            for u in self.Adj[v]:
                if self.dist[self.pair[u]] == self.dist[v] + 1:
                    if self.dfs(self.pair[u]) == True:
                        self.pair[u] = v
                        self.pair[v] = u
                        return True
            self.dist[v] = self.INF
            return False
        return True

    def run(self):
        for v in self.G:
            self.pair[v] = None
            self.dist[v] = self.INF
        matching = 0
        while self.bfs():
            for v in self.U:
                if self.pair[v] == None:
                    if self.dfs(v) == True:
                        matching = matching + 1
        return matching

    def print_info(self):
        pprint.pprint(self.U)
        pprint.pprint(self.V)
        pprint.pprint(self.G)
        pprint.pprint(self.pair)



bipart_graph = {'a0': set(['b0', 'b1']), 
                'a1': set(['b2', 'b3']), 
                'a2': set(['b0', 'b4']), 
                'a3': set(['b1', 'b2']), 
                'a4': set(['b3', 'b4']),
                'b0': set(['a0', 'a2']),
                'b1': set(['a0', 'a3']),
                'b2': set(['a1', 'a3']),
                'b3': set(['a1', 'a4']),
                'b4': set(['a2', 'a4'])}


a = Hopcroft_Karp(bipart_graph)
print a.run()
a.print_info()
