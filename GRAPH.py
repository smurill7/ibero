"""
Unittests for graph.classes.Graph
"""


import unittest
import pygraph
import copy

class testGraph(unittest.TestCase):

    def setUp(self):
        pass

    def testRandomGraph(self):
        gr = pygraph.graph()
        gr.generate(100, 500)
        self.assertEqual(gr.nodes(),range(100))
        self.assertEqual(len(gr.edges()), 500*2)
        for each, other in gr.edges():
            self.assertTrue(each in gr)
            self.assertTrue(other in gr)
    
    def testRandomEmptyGraph(self):
        gr = pygraph.graph()
        gr.generate(0,0)
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testNodeRemoval(self):
        gr = pygraph.graph()
        gr.generate(10, 30)
        gr.del_node(0)
        self.assertTrue(0 not in gr)
        for each, other in gr.edges():
            self.assertTrue(each in gr)
            self.assertTrue(other in gr)

    def testGraphInverse(self):
        gr = pygraph.graph()
        gr.generate(50, 300)
        inv = gr.inverse()
        for each in gr.edges():
            self.assertTrue(each not in inv.edges())
        for each in inv.edges():
            self.assertTrue(each not in gr.edges())
    
    def testEmptyGraphInverse(self):
        gr = pygraph.graph()
        inv = gr.inverse()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testGraphComplete(self):
        gr = pygraph.graph()
        gr.add_nodes(xrange(10))
        gr.complete()
        for i in xrange(10):
            for j in range(10):
                self.assertTrue((i, j) in gr.edges() or i == j)
    
    def testEmptyGraphComplete(self):
        gr = pygraph.graph()
        gr.complete()
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testGraphWithOneNodeComplete(self):
        gr = pygraph.graph()
        gr.add_node(0)
        gr.complete()
        self.assertTrue(gr.nodes() == [0])
        self.assertTrue(gr.edges() == [])
    
    def testAddGraph(self):
        gr1 = pygraph.graph()
        gr1.generate(25, 100)
        gr2 = pygraph.graph()
        gr2.generate(40, 200)
        gr1.add_graph(gr2)
        for each in gr2.nodes():
            self.assertTrue(each in gr1)
        for each in gr2.edges():
            self.assertTrue(each in gr1.edges())
    
    def testAddEmptyGraph(self):
        gr1 = pygraph.graph()
        gr1.generate(25, 100)
        gr1c = copy.copy(gr1)
        gr2 = pygraph.graph()
        gr1.add_graph(gr2)
        self.assertTrue(gr1.nodes() == gr1c.nodes())
        self.assertTrue(gr1.edges() == gr1c.edges())
    
    def testAddSpanningTree(self):
        gr = pygraph.graph()
        st = {0: None, 1: 0, 2:0, 3: 1, 4: 2, 5: 3}
        gr.add_spanning_tree(st)
        for each in st:
            self.assertTrue((each, st[each]) in gr.edges() or (each, st[each]) == (0, None))
            self.assertTrue((st[each], each) in gr.edges() or (each, st[each]) == (0, None))

    def testAddEmptySpanningTree(self):
        gr = pygraph.graph()
        st = {}
        gr.add_spanning_tree(st)
        self.assertTrue(gr.nodes() == [])
        self.assertTrue(gr.edges() == [])
    
    def testEdgeToItselfRemoval(self):
        gr = pygraph.graph()
        gr.add_node(0)
        gr.add_edge(0, 0)
        gr.del_edge(0, 0)
    
    def testNodeWithEdgeToItselfRemoval(self):
        gr = pygraph.graph()
        gr.add_node(0)
        gr.add_edge(0, 0)
        gr.del_node(0)
        
    def testTrivalEquality0(self):
        gr1 = pygraph.graph()
        gr2 = pygraph.graph()
        assert gr1 == gr2, "All zero node graphs should be equivalent to each other."
    
    def testTrivalEquality1(self):
        gr1 = pygraph.graph()
        gr1.add_node(0)
        gr2 = pygraph.graph()
        gr2.add_node(0)
        assert gr1 == gr2, "All one node graphs should be equivalent to each other."
    
    def testTrivalEquality2(self):
        gr1 = pygraph.graph()
        gr1.add_node(0)
        gr1.add_node(1)
        gr1.add_edge(0,1)
        gr2 = pygraph.graph()
        gr2.add_node(0)
        gr2.add_node(1)
        gr2.add_edge(0,1)
        assert gr1 == gr2, "Two identically constructed graphs should be equivalent to each other."