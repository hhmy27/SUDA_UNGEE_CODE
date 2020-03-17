import math


class Solution:
    def __init__(self):
        self.dataFilename = r"..\..\Data\data.txt"
        self.k = 0
        self.dimension = 0
        self.points = None
        self.nearestPoints = None
        self.readData()
        self.findNearestPoints()
        self.findKthNearestPoint()

    def readData(self):
        with open(self.dataFilename) as file:
            content = file.read()
            nums = list(map(int, content.split()))
            self.k = nums[0]
            self.dimension = nums[1]
            self.points = [tuple(nums[i:i + self.dimension]) for i in range(2, len(nums), self.dimension)]

    def findNearestPoints(self):
        minDis = -1
        p1, p2 = None, None
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                dis = Solution.calDis(self.points[i], self.points[j])
                if minDis == -1 or dis < minDis:
                    minDis = dis
                    p1, p2 = self.points[i], self.points[j]

        print("距离最近的两个点坐标为：{} {}, 距离为{}".format(p1, p2, minDis))
        self.nearestPoints = (p1, p2)

    def findKthNearestPoint(self):

        l1 = sorted(((Solution.calDis(p, self.nearestPoints[0]), p) for p in self.points if p != self.nearestPoints[0]),
                    key=lambda x: x[0])

        l2 = sorted(((Solution.calDis(p, self.nearestPoints[1]), p) for p in self.points if p != self.nearestPoints[1]),
                    key=lambda x: x[0])

        print("距离点{}最近的{}个点坐标为：{}".format(self.nearestPoints[0], self.k, [item[1] for item in l1[:self.k]]))
        print("距离点{}最近的{}个点坐标为：{}".format(self.nearestPoints[1], self.k, [item[1] for item in l2[:self.k]]))

    @staticmethod
    def calDis(p1: tuple, p2: tuple):
        s = sum(((i[0] - i[1]) ** 2 for i in zip(p1, p2)))
        return math.sqrt(s)


if __name__ == "__main__":
    solution = Solution()
