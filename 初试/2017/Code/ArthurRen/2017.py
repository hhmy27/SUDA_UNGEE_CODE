import unittest
import random
import queue
import testcases
from typing import List
from DataStructure.algraph import ALGraph
from DataStructure.mgraph import MGraph
from DataStructure.binarytree import BTNode


class Test2017(unittest.TestCase):

    def test_solution1(self):

        # <editor-fold desc="Answer to the question">
        def verify(num: int) -> bool:
            if num == 1:
                return True
            if num % 2 == 0 and verify(num // 2):
                return True
            if num % 3 == 0 and verify(num // 3):
                return True
            if num % 5 == 0 and verify(num // 5):
                return True
            return False

        def printNums(count: int):
            num = 1
            tick = 0
            while tick <= count:
                if verify(num):
                    tick += 1
                    print(num, end=' ')
                num += 1
        # </editor-fold>

        print("Solution 1:")
        printNums(100)
        print()

    def test_solution2(self):

        def createRandomNums(count: int) -> List[int]:
            return list(random.sample([i for i in range(count * 3)], count))

        def createBST(nums: List[int]) -> BTNode or None:
            if len(nums) == 0:
                return None
            node = BTNode(nums[0])
            lnums, rnums = [], []
            for i in nums[1:]:
                (lnums if i < nums[0] else rnums).append(i)
            node.lchild = createBST(lnums)
            node.rchild = createBST(rnums)
            node.rsizeplusone = len(rnums) + 1
            return node

        # <editor-fold desc="Answer to the question">
        def findKthLargestNum(node: BTNode, k: int) -> int:
            if node.rsizeplusone == k:
                return node.value
            elif node.rsizeplusone > k:
                return findKthLargestNum(node.rchild, k)
            else:
                return findKthLargestNum(node.lchild, k - node.rsizeplusone)
        # </editor-fold>

        rndNums = createRandomNums(20)
        bst = createBST(rndNums)
        rndNums.sort()
        print("Solution 2:")
        print("nums : {}".format(rndNums))
        for k in range(1, len(rndNums) + 1):
            num = findKthLargestNum(bst, k)
            self.assertEqual(num, rndNums[len(rndNums) - k])
            print("{}th largest num : {}".format(k, num))

    def test_solution3(self):

        # Answer to the question
        def findPath(graph: ALGraph, i: int, j: int) -> bool:
            visited = [0 for _ in range(len(graph.vertices))]
            q = queue.Queue()
            q.put(i)

            while not q.empty():
                v = q.get()
                if v == j:
                    return True
                visited[v] = True

                arc = graph.vertices[v].firstArc
                while arc:
                    if arc.adjVex == j:
                        return True
                    if not visited[arc.adjVex]:
                        q.put(arc.adjVex)
                    arc = arc.nextArc

            return False

        for case, rightResult in testcases.cases3.items():
            matrix = case[0]
            vertices = case[1]
            mg = MGraph(vertices, matrix)
            g = ALGraph.fromMGraph(mg)
            start = case[2]
            end = case[3]
            exist = findPath(g, start, end)
            self.assertEqual(exist, rightResult)
