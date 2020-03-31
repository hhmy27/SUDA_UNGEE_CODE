from typing import List
from types import FunctionType
from queue import Queue


class BTNode:
    """
    Node of binary tree
    """

    def __init__(self, value, lchild=None, rchild=None):
        self.__value = value
        self.__lchild = lchild
        self.__rchild = rchild

    # <editor-fold desc="property">
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def lchild(self):
        return self.__lchild

    @lchild.setter
    def lchild(self, lchild):
        self.__lchild = lchild

    @property
    def rchild(self):
        return self.__rchild

    @rchild.setter
    def rchild(self, rchild):
        self.__rchild = rchild

    # </editor-fold>

    def copy(self):
        """
        :return: Shadow copy
        """
        return BTNode(self.value, self.lchild, self.rchild)

    def preOrder(self, visit: FunctionType):
        BTNode.__preOrder(self, visit)

    def inOrder(self, visit: FunctionType):
        BTNode.__inOrder(self, visit)

    def postOrder(self, visit: FunctionType):
        BTNode.__postOrder(self, visit)

    def levelOrder(self, visit: FunctionType):
        BTNode.__levelOrder(self, visit)

    def levelOrderIterator(self):
        return BTNode.__levelOrderIterator(self)

    # <editor-fold desc="staticmethod">

    @staticmethod
    def __preOrder(root, visit: FunctionType):
        if not root:
            return

        assert isinstance(root, BTNode)
        assert visit is not None

        visit(root)
        BTNode.__preOrder(root.lchild, visit)
        BTNode.__preOrder(root.rchild, visit)

    @staticmethod
    def __inOrder(root, visit: FunctionType):
        if not root:
            return

        assert isinstance(root, BTNode)
        assert visit is not None

        BTNode.__inOrder(root.lchild, visit)
        visit(root)
        BTNode.__inOrder(root.rchild, visit)

    @staticmethod
    def __postOrder(root, visit: FunctionType):
        if not root:
            return

        assert isinstance(root, BTNode)
        assert visit is not None

        BTNode.__postOrder(root.lchild, visit)
        BTNode.__postOrder(root.rchild, visit)
        visit(root)

    @staticmethod
    def __levelOrder(root, visit: FunctionType):
        if not root:
            return

        assert isinstance(root, BTNode)
        assert visit is not None

        for node in BTNode.__levelOrderIterator(root):
            visit(node)

    @staticmethod
    def __levelOrderIterator(root):
        if not root:
            return

        assert isinstance(root, BTNode)

        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            yield node
            if node.lchild:
                q.put(node.lchild)
            if node.rchild:
                q.put(node.rchild)

    # </editor-fold>


def fromValueList(values: List or tuple):
    """
    Create a BTree from a sequential storage structure
    """

    def __fromList(index) -> BTNode or None:
        assert index is not None
        assert type(index) == int
        assert index >= 0

        if index >= len(values):
            return None
        else:
            return BTNode(values[index], __fromList((index + 1) * 2 - 1), __fromList((index + 1) * 2)) \
                if values[index] else None

    assert values is not None and type(values) == list or type(values) == tuple
    return __fromList(0)
