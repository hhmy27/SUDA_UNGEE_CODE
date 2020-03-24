import abc
from types import FunctionType


class Graph(abc.ABC):
    """
    Abstract class of Graph
    """
    def __init__(self):
        self.__arcNum = 0  # nums of arcs
        self.__vexNum = 0  # nums of vertices

    @property
    def arcNum(self):
        return self.__arcNum

    @property
    def vexNum(self):
        return self.__vexNum

    @abc.abstractmethod
    def vertices(self):
        # use 'abc.abstractmethod' to decorate the class as an abstract class
        pass

    def _setArcNum(self, num: int):
        """
        set the arc number
        """
        assert type(num) == int
        self.__arcNum = num

    def _setVexNum(self, num: int):
        """
        set the vex number
        """
        assert type(num) == int
        self.__vexNum = num


