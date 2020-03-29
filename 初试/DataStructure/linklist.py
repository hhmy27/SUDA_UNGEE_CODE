from collections import Iterable


class LinkNode(object):
    """
    Link Node of single link list
    """

    def __init__(self, value, nextNode=None):
        self.__value = value
        self.__next = nextNode

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nextNode):
        self.__next = nextNode

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __next__(self):
        if self.next is None:
            raise StopIteration()
        else:
            return self.next


def createLinkList(values: Iterable, hasHead: bool = False) -> LinkNode:
    """
    Create a single link list without head node
    :param values: values of the list
    :param hasHead: indicate whether the list contains head node
    :return: first node of the list
    """
    assert isinstance(values, Iterable)
    first = None
    pre = None
    for value in values:
        node = LinkNode(value)
        if first is None:
            first = node
        if pre is not None:
            pre.next = node
        pre = node
    if hasHead:
        head = LinkNode(None, first)
        return head
    else:
        return first
