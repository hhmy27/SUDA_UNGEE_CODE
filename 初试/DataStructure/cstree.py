from typing import Sequence
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


def createCSTree(nodes: Sequence[Sequence[Sequence[int]]]) \
        -> CSTreeNode or None:
    """
    Create a cstree from nodes stored in level order
    Each element represents a tree node, and contains 2 elements
        Tuple[0] : child count of the node
        Tuple[1] : node value

    Example:
            (
                ((3, 1),),  # Root node , contains 3 children and it's value is 1
                ((2, 2), (1, 3), (0, 4)),
                ((3, 5), (0, 6), (0, 7)),
                ((0, 8), (0, 9), (0, 10))
            )
    """
    levels = len(nodes)
    visitedIndices = [0 for _ in range(levels)]  # storage the start index of unvisited nodes in each level

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
        childCount = nodeTuple[0]
        value = nodeTuple[1]

        nextRow = r + 1
        firstChild = None
        if nextRow < levels:
            firstChild = createNode(r + 1, visitedIndices[nextRow], childCount - 1) if childCount > 0 else None
            visitedIndices[nextRow] += childCount

        # If the node has sibling , create sibling node
        nextSibling = createNode(r, c + 1, siblingCount - 1) if siblingCount > 0 else None
        return CSTreeNode(value, firstChild, nextSibling)

    return createNode(0, 0, 0)
