import unittest
from binarytree import BTNode

valueList = [1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, None, 9]
tree = None


class TestBTNode(unittest.TestCase):
    def setUp(self):
        global tree
        tree = BTNode.fromValueList(valueList)

    def test_preOrder(self):
        orders = []
        tree.preOrder(lambda x: orders.append(x.value))
        self.assertEqual([1, 2, 4, 5, 7, 8, 3, 6, 9], orders)

    def test_inOrder(self):
        orders = []
        tree.inOrder(lambda x: orders.append(x.value))
        self.assertEqual([4, 2, 7, 5, 8, 1, 3, 6, 9], orders)

    def test_postOrder(self):
        orders = []
        tree.postOrder(lambda x: orders.append(x.value))
        self.assertEqual([4, 7, 8, 5, 2, 9, 6, 3, 1], orders)

    def test_levelOrder(self):
        orders = []
        tree.levelOrder(lambda x: orders.append(x.value))
        self.assertEqual([value for value in valueList if value], orders)