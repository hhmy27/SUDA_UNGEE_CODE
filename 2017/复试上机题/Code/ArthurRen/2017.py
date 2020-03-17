import math


class Solution:
    def __init__(self):
        self.dataFilename = r"..\..\Data\data.bin"
        self.outputFilename = "data.txt"
        self.points = []
        self.circles = []
        self.readPoints()

    def readPoints(self):
        with open(self.dataFilename, "rb") as file:
            rawData = file.read()
            self.points = [(rawData[i], rawData[i+1]) for i in range(len(rawData))[::2]]
            densities = []
            for i in range(len(self.points)):
                p1 = self.points[i]
                p2 = self.points[(i + 1) % len(self.points)]
                r = Solution.calDis(p1, p2)
                for point in self.points:
                    count = 2
                    if point != p1 and point != p2 and Solution.calDis(p1, point) <= r:
                        count += 1

                area = 3.14 * r ** 2
                densities.append((p1, count, count / area))

        lst = sorted(densities, key=lambda x: x[2], reverse=True)
        with open(self.outputFilename, "w") as fo:
            for item in lst[:5]:
                fo.write("{}{:>5}{:>7.2f}\n".format(item[0], item[1], item[2]))

    @staticmethod
    def calDis(p1: tuple, p2: tuple) -> float:
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == "__main__":
    solution = Solution()