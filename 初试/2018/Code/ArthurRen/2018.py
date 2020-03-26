import unittest
import testcases
import DataStructure.cstree as cstree
import DataStructure.binarytree as btree
import DataStructure.linklist as linklist
from DataStructure.linklist import LinkNode


class Test2019(unittest.TestCase):

    def test_solution1(self):

        # Answer to the question
        def judge(first: LinkNode) -> bool:
            node = first
            flag = True  # Indicate if we have met the even number
            while node:
                if node.value % 2 == 1:
                    # If the current value is odd and we have met the even number, return False
                    if not flag:
                        return False
                else:
                    # If we meet first even number, flip flag
                    if flag:
                        flag = False
                node = node.next
            return True

        for case, rightResult in testcases.cases1.items():
            lst = linklist.createLinkList(case)
            result = judge(lst)
            self.assertEqual(rightResult, result)

    def test_solution2(self):

        # Answer to the question
        def getAndSetSize(node: btree.BTNode) -> int:
            if node is None:
                return 0
            else:
                # Get the nodes count in left child
                lcount = getAndSetSize(node.lchild)
                # Get the nodes count in right child
                rcount = getAndSetSize(node.rchild)
                # Set size property
                node.size = lcount + rcount
                # Return total nodes count in the node
                return node.size + 1

        for case, rightResult in testcases.cases2.items():
            tree = btree.BTNode.fromValueList(case)
            getAndSetSize(tree)
            result = [node.size for node in tree.levelOrderIterator()]
            print(result)
            # Compare all the elements in the result & rightResult sequence
            self.assertTrue(
                all(i == j for i, j in zip(result, rightResult)) and
                len(result) == len(rightResult)
            )

    def test_solution3(self):
        """
        Attention :
            The definition of degree of tree node in 百度百科 is ambiguous, please refer to the《数据结构》 by 严蔚敏
        :return:
        """

        # Answer to the question
        def countKDegreeNode(t: cstree.CSTreeNode, k: int) -> int:
            degree = 0
            count = 0

            node = t.firstChild
            while node:
                # Increase the degree of current node
                degree += 1
                # Get count of k degree nodes in the sub node
                count += countKDegreeNode(node, k)
                # Move to the next child node
                node = node.nextSibling

            if degree == k:
                count += 1

            return count

        for case, rightResult in testcases.cases3.items():
            tree = cstree.createCSTree(case[0])
            result = [countKDegreeNode(tree, k) for k in case[1]]
            self.assertTrue(
                all(i == j for i, j in zip(result, rightResult)) and
                len(result) == len(rightResult)
            )
