import unittest
import testcases
import DataStructure.linklist as linklist
from DataStructure.linklist import LinkNode
from DataStructure.binarytree import BTNode


class Test2012(unittest.TestCase):

    def test_solution1(self):

        def switchNode(lst: LinkNode, index: int) -> LinkNode:
            # Add a head node for the list
            head = LinkNode(None, lst)
            p = head
            i = 0
            while i < index - 1:
                p = p.next
                i += 1
            nextNode = p.next
            p.next = nextNode.next
            nextNode.next = p.next.next
            p.next.next = nextNode
            return head.next

        for case, rightResult in testcases.cases1.items():
            lst = linklist.createSingleLinkList(case[0], False)
            lst = switchNode(lst, case[1])
            result = tuple(node.value for node in lst)
            self.assertEqual(rightResult, result)

    def test_solution2(self):

        def createBST(start: int, end: int) -> BTNode:
            # The search tree of the binary search is balanced
            mid = (start + end) // 2
            root = BTNode(mid)
            if start <= mid - 1:
                root.lchild = createBST(start, mid - 1)
            if mid - 1 >= end:
                root.rchild = createBST(mid + 1, end)
            return root

        def isBalancedTree(root: BTNode) -> (bool, int):
            """
            Judge if a btree is balanced
            :param root: root node of a btree
            :return: bool : is balanced ; int: height of the tree
            """
            if root is None:
                return True, 0

            leftBalanced, leftHeight = isBalancedTree(root.lchild)
            if not leftBalanced:
                return False, None

            rightBalanced, rightHeight = isBalancedTree(root.rchild)
            if not rightBalanced:
                return False, None

            return True, (leftHeight if leftHeight > rightHeight else rightHeight) + 1

        for i in range(1, 10):
            tree = createBST(0, i)
            self.assertTrue(isBalancedTree(tree))
