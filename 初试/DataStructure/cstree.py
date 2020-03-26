from typing import List
from typing import Tuple
from queue import Queue


class CSTreeNode:
    """
    Node of child-sibling tree
    """
    def __init__(self, value, firstChild, nextSibling):
        """
        :param firstChild: first child of the tree node
        :param nextSibling: next sibling of the tree node
        """
        assert type(firstChild) == CSTreeNode or firstChild is None
        assert type(nextSibling) == CSTreeNode or nextSibling is None

        self.__firstChild = firstChild
        self.__nextSibling = nextSibling
        self.__value = value

    @property
    def firstChild(self):
        return self.__firstChild

    @firstChild.setter
    def firstChild(self, node):
        assert type(node) == CSTreeNode
        self.__firstChild = node

    @property
    def nextSibling(self):
        return self.__nextSibling

    @nextSibling.setter
    def nextSibling(self, node):
        assert type(node) == CSTreeNode
        self.__nextSibling = node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, obj):
        self.__value = obj

    def levelOrderIterator(self):
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            node = queue.get()
            yield node
            node = node.firstChild
            while node:
                queue.put(node)
                node = node.nextSibling



def createCSTree(nodes: Tuple[List[Tuple] or Tuple[Tuple]] or List[List[Tuple] or Tuple[Tuple]]) \
        -> CSTreeNode or None:
    """
    Create a cstree from nodes stored in level order
    Each tuple represents a tree node, and contains 2 elements
        Tuple[0] : child count of the node
        Tuple[1] : node value
    """
    levels = len(nodes)
    childIndices = {}

    def createNode(r: int, c: int, siblingCount: int) -> CSTreeNode or None:
        """
        Create cstree node from values
        :param r: row index
        :param c: column index
        :param siblingCount: the sibling count of the node
        :return: cstree node
        """
        if r >= levels:
            return None
        if c >= len(nodes[r]):
            return None

        nodeTuple = nodes[r][c]
        childCount = nodeTuple[0]; value = nodeTuple[1]

        nextRow = r + 1
        firstChild = createNode(r + 1, childIndices.get(nextRow, 0), childCount - 1) if childCount > 0 else None
        childIndices[nextRow] = childIndices.get(nextRow, 0) + childCount

        # If the node has sibling , create sibling node
        nextSibling = createNode(r, c + 1, siblingCount - 1) if siblingCount > 0 else None
        return CSTreeNode(value, firstChild, nextSibling)

    return createNode(0, 0, 0)
