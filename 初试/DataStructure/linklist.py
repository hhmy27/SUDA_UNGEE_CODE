from collections import Iterable


class LinkNode(object):
    """
    Link Node of single link list
    """

    def __init__(self, value, nextNode=None):
        assert nextNode is None or issubclass(type(nextNode), LinkNode)

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
        assert nextNode is None or issubclass(type(nextNode), LinkNode)

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


def createSingleLinkList(values: Iterable, hasHead: bool = False) -> LinkNode:
    """
    Create a single link list
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
        head = LinkNode(None, nextNode=first)
        return head
    else:
        return first


class DLinkNode(LinkNode):
    """
    Double link node
    """

    def __init__(self, value, nextNode=None, priorNode=None):
        """
        :param value: value of the node
        :param nextNode: next node
        :param priorNode: precursor node
        """
        assert priorNode is None or isinstance(priorNode, DLinkNode)

        super().__init__(value, nextNode)
        self.__prior = priorNode

    @property
    def prior(self):
        return self.__prior

    @prior.setter
    def prior(self, node):
        assert node is None or isinstance(node, DLinkNode)
        self.__prior = node


def createDoubleLinkList(values: Iterable, hasHead: bool = False) -> DLinkNode:
    """
    Create a double link list
    :param values: values of the list
    :param hasHead: indicate whether the list contains head node
    :return: first node of the list
    """
    assert isinstance(values, Iterable)
    assert isinstance(hasHead, bool)

    first = None
    pre = None
    for value in values:
        node = DLinkNode(value, priorNode=pre)
        if first is None:
            first = node
        if pre is not None:
            pre.next = node
        pre = node
    if hasHead:
        head = DLinkNode(None, nextNode=first)
        first.prior = head
        return head
    else:
        return first
