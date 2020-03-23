from graph import Graph
from types import FunctionType
from typing import List


class MGraph(Graph):
    """
    Graph implemented with matrix
    """
    def __init__(self, vertices: List, arcMatrix: List[List]):
        """
        :param vertices: vertex list
        :param arcMatrix: arc matrix
        """
        super().__init__()

        vexNum = len(vertices)

        # Verify if the arcs matrix has the same size with vertices
        assert vexNum == len(arcMatrix)
        assert all(vexNum == (len(arcs) if arcs else 0) for arcs in arcMatrix)

        arcNum = sum(len(arcs) - arcs.count(False) for arcs in arcMatrix)

        self._setVexNum(vexNum)
        self._setArcNum(arcNum)

        self.__vertices = vertices
        self.__arcMatrix = arcMatrix

    @property
    def vertices(self):
        return self.__vertices

    @property
    def arcMatrix(self):
        return self.__arcMatrix

    def bfs(self, visit: FunctionType):
        raise NotImplementedError()

    def dfs(self, visit: FunctionType):
        visited = [False for _ in range(self.vexNum)]

        def __dfs(v):
            """
            dfs from a specified vertex
            :param v:index of vertex
            """
            assert v < self.vexNum
            if visited[v]:
                return
            # visit vertex
            if visit:
                visit(self.vertices[v])
            # set flag
            visited[v] = True
            # find the next vertex
            for index, arc in enumerate(self.arcMatrix[v]):
                if arc and index != v:
                    __dfs(index)

        for i in range(self.vexNum):
            __dfs(i)
