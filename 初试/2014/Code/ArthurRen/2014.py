import unittest
import testcases
import math
import random
import DataStructure.binarytree as btree
from typing import List
from DataStructure.linklist import LinkNode
from DataStructure.binarytree import BTNode


class Test2014(unittest.TestCase):

    def test_solution1(self):

        # <editor-fold desc="Answer to the question">
        def isPrime(num: int) -> bool:
            if num == 2 or num == 3:
                return True
            else:
                for i in range(2, math.ceil(math.sqrt(num))):
                    if num % i == 0:
                        return False
                else:
                    return True

        def primeFactorization(num: int) -> LinkNode:
            head = LinkNode(None)  # head node of primes link list
            x = 2
            while num != 1:
                # Find the minimal prime that can divide the num
                if head.next is not None and num % head.next.value == 0:
                    val = head.next.value
                    x = val + 1
                else:
                    while True:
                        if isPrime(x) and num % x == 0:
                            val = x
                            break
                        x += 1

                # Insert to head
                newNode = LinkNode(val, head.next)
                head.next = newNode
                num //= val
            return head
        # </editor-fold>

        for case, rightResult in testcases.cases1.items():
            lst = primeFactorization(case)
            results = lst.next.toList()
            self.assertEqual(rightResult, results, "Error case: {}".format(case))

    def test_solution2(self):

        # Answer to the question
        def judge(node: BTNode) -> bool:
            if node is None:
                return True
            if (node.lchild is None) ^ (node.rchild is None):
                return False
            return judge(node.lchild) and judge(node.rchild)

        for case, rightResult in testcases.cases2.items():
            tree = btree.fromValueList(case)
            result = judge(tree)
            self.assertEqual(rightResult, result, "Error case: {}".format(case))

    def test_solution3(self):

        # Answer to the question
        def findKthNum(nums: List[int], k: int, start: int, end: int) -> int:
            """
            Algorithm idea: quick sort
            """
            assert k <= len(nums)
            i, j = start, end
            pivot = nums[start]
            while i < j:
                while i < j and pivot <= nums[j]:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                while i < j and pivot >= nums[i]:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
            nums[i] = pivot

            if i + 1 == k:
                return pivot
            elif k < i + 1:
                return findKthNum(nums, k, start, i - 1)
            else:
                return findKthNum(nums, k, i + 1, end)

        # Test random data
        for i in range(10):
            case = [random.randint(0, 100) for _ in range(10)]
            sortedCase = sorted(case)
            for j in range(len(case)):
                self.assertEqual(sortedCase[j], findKthNum(case, j + 1, 0, len(case) - 1))
