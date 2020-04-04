import unittest
import testcases
import DataStructure.linklist as linklist
import DataStructure.cstree as cstree
from DataStructure.cstree import CSTreeNode
from DataStructure.linklist import LinkNode


class Test2013(unittest.TestCase):
    def test_solution1(self):

        # Answer to the question
        def getNodesCount(node: CSTreeNode) -> int:
            if node is None:
                return 0
            child = node.firstChild
            count = 0
            while child:
                count += getNodesCount(child)
                child = child.nextSibling
            return count + 1

        for case, rightResult in testcases.cases1.items():
            tree = cstree.createCSTree(case)
            count = getNodesCount(tree)
            self.assertEqual(rightResult, count)

    def test_solution2(self):

        # Answer to the question
        def remove(node: LinkNode, item: int) -> int or None:
            """
            Remove the node whose value is item
            :param node: head node
            :param item: node value to remove
            :return: node value of current item
            """
            if node is None:
                return None
            nextVal = remove(node.next, item)
            if nextVal == item and node.next is not None:
                node.next = node.next.next
            return node.value

        for case, rightResult in testcases.cases2.items():
            lst = linklist.createSingleLinkList(case[0], True)
            remove(lst, case[1])
            result = tuple(node.value for node in lst.next)
            self.assertEqual(rightResult, result)

    def test_solution3(self):

        # Answer to the question
        def getNewValueCount(num: int) -> int:
            count = 1
            while num // 10 != 0:
                temp = 0
                while num != 0:
                    temp += num % 10
                    num //= 10
                count += 1
                num = temp
            return count

        for case, rightResult in testcases.cases3.items():
            count = getNewValueCount(case)
            self.assertEqual(count, rightResult)
