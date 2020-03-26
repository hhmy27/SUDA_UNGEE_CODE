import unittest
from DataStructure.mgraph import MGraph

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
graph = None


class TestMGraph(unittest.TestCase):
    def setUp(self):
        global graph
        graph = MGraph(vertices, arcMatrix)

    def test_dfs(self):
        rightOrders = [1, 2, 4, 8, 5, 3, 6, 7, 10, 9]
        dfsOrders = []
        graph.dfs(lambda x: dfsOrders.append(x))
        self.assertEqual(rightOrders, dfsOrders)
