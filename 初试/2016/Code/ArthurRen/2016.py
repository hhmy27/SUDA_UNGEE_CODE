import unittest
import testcases
import DataStructure.linklist as linklist
from DataStructure.linklist import LinkNode
from typing import Sequence


class Test2016(unittest.TestCase):

    def test_solution1(self):
        """
        time complexity : O(n^2)
        space complexity : O(1)
        """

        # <editor-fold desc="Answer to the question">
        def exist(lst: LinkNode, num) -> bool:
            p = lst.next
            while p:
                if p.value == num:
                    return True
                p = p.next
            return False

        def removeDuplicatedElements(A: LinkNode) -> LinkNode:
            head = LinkNode(None)  # head node of new list
            p = head
            q = A.next
            while q:
                if not exist(head, q.value):  # if there is no same element in the new link list
                    newNode = LinkNode(q.value)
                    p.next = newNode  # append to the new link list
                    p = newNode
                q = q.next

            return head

        # </editor-fold>

        for case, rightResult in testcases.cases1.items():
            A = linklist.createSingleLinkList(case, True)  # create a link list with head node
            result = removeDuplicatedElements(A)
            self.assertEqual(rightResult, [node.value for node in result.next])

    def test_solution2(self):

        # <editor-fold desc="Answer to the question">
        def getMinSubsequence_1(nums: Sequence[int]) -> int:
            """
            Kadane's Algorithm (dynamic programming)
            time complexity : O(n)
            space complexity : O(n)
            """
            if len(nums) == 2:
                return 0 if all((x > 0 for x in nums)) else sum(nums)
            if all((x > 0 for x in nums)):
                return 0
            dp = [0 for _ in nums]  # used to save the min sum of nums[0: i]
            dp[1] = nums[0] + nums[1]
            m = dp[1]
            for i in range(2, len(dp)):
                s = dp[i - 1] + nums[i]
                temp = nums[i - 1] + nums[i]
                dp[i] = s if s < temp else temp
                m = dp[i] if dp[i] < m else m
            return m

        def getMinSubsequence_2(nums: Sequence[int]) -> int:
            """
            Directly Calculating
            time complexity : O(n^2)
            space complexity : O(1)
            """
            m = sum(nums[0:2])
            if all((x > 0 for x in nums)):
                return 0
            for i in range(len(nums) - 1):
                s = nums[i]
                for j in range(i + 1, len(nums)):
                    s += nums[j]
                    m = s if s < m else m
            return m

        # </editor-fold>

        for case, rightResult in testcases.cases2.items():
            result1 = getMinSubsequence_1(case)
            result2 = getMinSubsequence_2(case)
            self.assertEqual(result1, rightResult)
            self.assertEqual(result2, rightResult)

    def test_solution3(self):

        # Answer to the question
        def getBTreeCountWithNNode(n: int) -> int:
            if n == 0:
                return 1
            elif n == 1 or n == 2:
                return n
            else:
                s = 0
                for i in range(0, n):
                    s += getBTreeCountWithNNode(i) * getBTreeCountWithNNode(n - i - 1)
                return s

        def catalan(n):
            if n <= 1:
                return 1
            res = 0
            for i in range(n):
                res += catalan(i) * catalan(n - i - 1)

            return res

        for i in range(10):
            self.assertEqual(getBTreeCountWithNNode(i), catalan(i))
