import DataStructure.cstree as tree
import unittest


class TestCSTree(unittest.TestCase):

    def test_createCSTree(self):
        nodes = [
            ((3, 1),),  # Root node , contains 3 children and it's value is 1
            ((2, 2), (1, 3), (0, 4)),
            ((3, 5), (0, 6), (0, 7)),
            ((0, 8), (0, 9), (0, 10)),
        ]
        cstree = tree.createCSTree(nodes)
        orders = []
        for rows in nodes:
            orders.extend([t[1] for t in rows])
        results = [node.value for node in cstree.levelOrderIterator()]
        self.assertEqual(orders, results)
