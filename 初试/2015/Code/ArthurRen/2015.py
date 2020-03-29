import unittest
import testcases
import random
import DataStructure.linklist as linklist
import DataStructure.binarytree as btree
from DataStructure.linklist import LinkNode
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

        def find_kth(left_lst, left_len, right_lst, right_len, k):
            """
            从left_lst 和 right_lst中寻找第k大的数
            :param left_lst: 长度小的那个数组
            :param left_len:
            :param right_lst: 长度达的那个数组
            :param right_len:
            :param k:
            :return:
            """
            # 确保left_lst长度小于 right_lst 长度
            if left_len > right_len:
                return find_kth(right_lst, right_len, left_lst, left_len, k)

            # 长度小的数组已经没有值了,从right_lst找到第k大的数
            if left_len == 0:
                return right_lst[k - 1]

            # 找到第1 大的数,比较两个列表的第一个元素,返回最小的那个
            if k == 1:
                return min(left_lst[0], right_lst[0])

            # k >> 1 ,其实就是k/2
            middle = min(k // 2, left_len)
            middle_ex = k - middle
            # 舍弃left_lst的一部分
            if left_lst[middle - 1] < right_lst[middle_ex - 1]:
                return find_kth(left_lst[middle:], left_len - middle, right_lst, right_len, k - middle)
            # 舍弃right_lst 的一部分
            elif left_lst[middle - 1] > right_lst[middle_ex - 1]:
                return find_kth(left_lst, left_len, right_lst[middle_ex:], right_len - middle_ex, k - middle_ex)
            else:
                return left_lst[middle - 1]

        for i in range(10):
            nums1 = [random.randint(0, 100) for _ in range(4)]
            nums1.sort()
            nums2 = [random.randint(0, 100) for _ in range(5)]
            nums2.sort()
            nums = nums1 + nums2
            nums.sort()
            mid = nums[len(nums) // 2] 
            result = find_kth(nums1, len(nums1), nums2, len(nums2), len(nums) // 2 + 1)
            self.assertEqual(mid, result)
