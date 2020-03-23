from graph import Graph
from mgraph import MGraph


class ArcNode:
    """
    Arc Node
    """
    def __init__(self, value, adjVex: int, nextArc):
        """
        :param value: value of the arc
        :param adjVex: index of adjvex in the ALGraph.vertices
        :param nextArc: next arc of the node
        """
        assert type(adjVex) == int
        assert type(nextArc) == ArcNode or nextArc is None

        self.__value = value
        self.__nextArc = nextArc
        self.__adjVex = adjVex

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def nextArc(self):
        return self.__nextArc

    @nextArc.setter
    def nextArc(self, arc):
        assert type(arc) == ArcNode
        self.__nextArc = arc

    @property
    def adjVex(self):
        return self.__adjVex

    @adjVex.setter
    def adjVex(self, value: int):
        self.__adjVex = value


class VNode:
    """
    Vertex Node
    """

    def __init__(self, value, firstArc: ArcNode or None):
        """
        :param value: value of the vertex
        :param firstArc: first arc of the vertex
        """
        assert type(firstArc) == ArcNode or firstArc is None

        self.__value = value
        self.__firstArc = firstArc

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def firstArc(self):
        return self.__firstArc

    @firstArc.setter
    def firstArc(self, arc: ArcNode):
        assert type(arc) == ArcNode or arc is None
        self.__firstArc = arc


class ALGraph(Graph):
    """
    Graph implemented with adjacent list
    """

    # noinspection PyMissingConstructor
    def __init__(self):
        # prevent class ALGraph from being instantiated directly
        raise Exception("Please use %s instead" % ALGraph.fromMGraph.__name__)

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__vertices = []
        return self

    @property
    def vertices(self):
        return self.__vertices

    def toMGraph(self) -> MGraph:
        """
        Convert this ALGraph to MGraph
        """
        # create an empty arc matrix and set the main diagonal to 1
        arcMatrix = [[int(i == j) for i in range(self.vexNum)] for j in range(self.vexNum)]
        vertices = [vnode.value for vnode in self.vertices]

        visited = [False for _ in range(self.vexNum)]

        def __bfs(v):
            assert v < self.vexNum
            if visited[v]:
                return
            visited[v] = True
            arcNode = self.vertices[v].firstArc
            while arcNode:
                arcMatrix[v][arcNode.adjVex] = arcNode.value
                arcNode = arcNode.nextArc

        for i in range(self.vexNum):
            __bfs(i)

        return MGraph(vertices, arcMatrix)

    @staticmethod
    def fromMGraph(mgraph: MGraph):
        """
        Convert MGraph to ALGraph
        :param mgraph: matrix graph
        :return: ALGraph
        """
        # noinspection PyTypeChecker
        algraph = ALGraph.__new__(ALGraph)

        for index, vexValue in enumerate(mgraph.vertices):
            vnode = VNode(vexValue, None)
            algraph.vertices.append(vnode)
            preArc = None
            for adjvex, arc in enumerate(mgraph.arcMatrix[index]):
                # if the current arc is not none and the adjvex is not self
                if arc and index != adjvex:
                    # create a new arc node
                    arcNode = ArcNode(arc, adjvex, None)
                    # if the preArc is not none, link the preArc.nextArc to the new arc node
                    if preArc:
                        preArc.nextArc = arcNode
                    preArc = arcNode
                    # set the first arc of current vex node
                    if not vnode.firstArc:
                        vnode.firstArc = arcNode

        algraph._setVexNum(mgraph.vexNum)
        algraph._setArcNum(mgraph.arcNum)
        return algraph
