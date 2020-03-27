import unittest
import DataStructure.linklist as linklist


class TestLinkList(unittest.TestCase):
    def test_createLinkList(self):
        cases = {
            (1, 2, 3, 4, 5, 6),
            (3, 4, 5)
        }

        for case in cases:
            result = tuple((node.value for node in linklist.createLinkList(case)))
            self.assertEqual(case, result)

        self.assertEqual(None, linklist.createLinkList([]))
