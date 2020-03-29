import unittest
import DataStructure.linklist as linklist


class TestLinkList(unittest.TestCase):
    def test_createSingleLinkList(self):
        cases = {
            (1, 2, 3, 4, 5, 6),
            (3, 4, 5)
        }

        for case in cases:
            result = tuple((node.value for node in linklist.createSingleLinkList(case)))
            self.assertEqual(case, result)

        self.assertEqual(None, linklist.createSingleLinkList([]))

    def test_createDoubleLinkList(self):
        cases = {
            (1, 2, 3, 4, 5, 6),
            (3, 4, 5)
        }

        for case in cases:
            lst = linklist.createDoubleLinkList(case)
            positiveOrder = tuple((node.value for node in lst))
            self.assertEqual(case, positiveOrder)

            reversedOrder = []
            p = lst
            while p.next:
                p = p.next

            while p:
                reversedOrder.append(p.value)
                p = p.prior

            self.assertEqual(tuple(reversed(case)), tuple(reversedOrder))

        self.assertEqual(None, linklist.createSingleLinkList([]))
