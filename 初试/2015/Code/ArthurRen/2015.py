import unittest
import testcases
import random
import DataStructure.linklist as linklist
import DataStructure.binarytree as btree
from typing import Sequence


class Test2015(unittest.TestCase):

    def test_solution1(self):
        for case, orders in testcases.cases1.items():
            # Answer to the question
            tree = btree.fromValueList(case)
            # Verify the result
            preorder = []
            tree.preOrder(lambda x: preorder.append(x.value))
            inorder = []
            tree.inOrder(lambda x: inorder.append(x.value))
            self.assertEqual(orders, [preorder, inorder])

    def test_solution2(self):

        # Answer to the question
        def findNums(head: linklist.DLinkNode, s: int) -> (int, int) or None:
            if head is None:
                return None
            p = head  # tail pointer
            while p.next:
                p = p.next
            q = head  # head pointer
            while p != q:
                temp = p.value + q.value
                if temp > s:
                    p = p.prior
                elif temp < s:
                    q = q.next
                else:
                    return q.value, p.value
            return None

        for case, rightResult in testcases.cases2.items():
            lst = linklist.createDoubleLinkList(case[0])
            result = findNums(lst, case[1])
            self.assertEqual(rightResult, result)

    def test_solution3(self):
        """
        There are 2 algorithms to solve the question:
        1. Merge the two array into a sorted array, then return the median of the array.
            Time complexity: O(m + n)
        2. Binary search :
            Time complexity: O(log(m + n))
        """

        def findMedian_1(a: Sequence[int], b: Sequence[int]) -> int:
            mergedNums = []
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    mergedNums.append(a[i])
                    i += 1
                else:
                    mergedNums.append(b[j])
                    j += 1
            mergedNums.extend(b[j:] if j < len(b) else a[i:])
            return mergedNums[len(mergedNums) // 2]

        def findMedian_2(a: Sequence[int], b: Sequence[int]) -> int:
            def findKth(A, sa, lena, B, sb, lenb, k):
                if lena > lenb:
                    return findKth(B, sb, lenb, A, sa, lena, k)
                if lena == 0:
                    return B[sb + k - 1]
                if k == 1:
                    return A[sa] if A[sa] < B[sb] else B[sb]

                mid = k // 2
                pa = mid if mid < lena else lena
                pb = k - pa

                mida = A[sa + pa - 1]
                midb = B[sb + pb - 1]
                if mida < midb:
                    return findKth(A, sa + pa, lena - pa, B, sb, lenb, k - pa)
                elif mida > midb:
                    return findKth(A, sa, lena, B, sb + pb, lenb - pb, k - pb)
                else:
                    return A[sa + pa - 1]

            return findKth(a, 0, len(a), b, 0, len(b), (len(a) + len(b)) // 2 + 1)

        for _ in range(10):
            nums1 = [random.randint(0, 100) for _ in range(4)]
            nums1.sort()
            nums2 = [random.randint(0, 100) for _ in range(5)]
            nums2.sort()
            nums = nums1 + nums2
            nums.sort()
            mid = nums[len(nums) // 2]

            result1 = findMedian_1(nums1, nums2)
            result2 = findMedian_2(nums1, nums2)
            self.assertEqual(mid, result1, "test1")
            self.assertEqual(mid, result2, "test2")
