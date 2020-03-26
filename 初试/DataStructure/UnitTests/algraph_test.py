import unittest
from DataStructure.mgraph import MGraph
from DataStructure.algraph import ALGraph
from DataStructure.graph import Graph

arcMatrix = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
]
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mgraph = MGraph(vertices, arcMatrix)
algraph = None


class TestALGraph(unittest.TestCase):
    def setUp(self):
        global algraph
        algraph = ALGraph.fromMGraph(mgraph)

    def test_toMGraph(self):
        result = algraph.toMGraph()
        self.assertEqual(result.arcMatrix, mgraph.arcMatrix)
        self.assertEqual(result.vertices, mgraph.vertices)
        self.assertEqual(result.vexNum, mgraph.vexNum)
        self.assertEqual(result.arcNum, mgraph.arcNum)

