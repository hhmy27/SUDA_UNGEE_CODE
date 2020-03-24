import unittest
import testcases  # If you use "Pycharm", please make the current directory as source root.
from typing import Set
from typing import Tuple
from DataStructure.binarytree import BTNode
import DataStructure.algraph as algraph
import DataStructure.mgraph as mgraph


def printResult(case, result):
    print("Case: {} -> Result: {}".format(case, result))


class Test2019(unittest.TestCase):

    def test_solution1(self):
        """
        Solution :
        Recursively visit the tree in the order of "node -> node.rchild -> node.lchild" ,
        the first node we meet which has no child nodes is the so called "last node under preorder traversing".
        """

        # Answer to the question
        def findLastNode(node: BTNode) -> bool:
            """
            Find the last node in the btree under preorder traversing
            :param node: node to verify
            :return: whether this node is the "last node"
            """
            if not node:
                return False
            path.append(node.value)
            # If the node has no child, it's the last node, so return True in order to stop recursion
            if not node.rchild and not node.lchild:
                return True
            else:
                # If the rchild is the last child, then return True,
                # otherwise return the result of lchild recursion
                return True if findLastNode(node.rchild) else findLastNode(node.lchild)

        print("Solution1: ")
        for case, rightResult in testcases.cases1.items():
            path = []
            tree = BTNode.fromValueList(case)
            findLastNode(tree)
            printResult(case, path)
            self.assertEqual(path, rightResult)

    def test_solution2(self):
        """
        Solution:
        Use "backtracking algorithm" to generate all the simple paths from node i to node j in the graph
        """

        # Answer to the question
        def findSimplePaths(g: algraph.ALGraph, i: int, j: int) -> Set[Tuple[int]]:
            """
            Find all the simple paths from i to j in graph
            :param g: graph to search
            :param i: start index of node in ALGraph.vertices
            :param j: end index of node in ALGraph.vertices
            :return: simple paths set
            """
            # Use bool list to prevent vnode from being duplicately visited
            visited = [False for _ in range(g.vexNum)]
            simplePaths = set()  # used to storage simple paths
            path = []  # used to storage the node indices in the current visiting path

            def dfs(v):
                if visited[v]:
                    return

                # Add current node index to the path
                path.append(v)
                visited[v] = True

                # If it's the end node, copy the current path to the result set
                if v == j:
                    simplePaths.add(tuple(path))
                # Search other nodes
                else:
                    arc = g.vertices[v].firstArc
                    while arc:
                        dfs(arc.adjVex)
                        arc = arc.nextArc

                # Remove the current node in order to search some other paths
                path.pop()
                visited[v] = False

            dfs(i)
            return simplePaths

        print("Solution2: ")
        for case, rightResult in testcases.cases2.items():
            # Generate algraph
            matrix, vertices = case[0], case[1]
            mg = mgraph.MGraph(vertices, matrix)
            graph = algraph.ALGraph.fromMGraph(mg)
            # Process
            start, end = case[2], case[3]
            result = findSimplePaths(graph, start, end)
            printResult(case, result)
            self.assertEqual(rightResult, result)
