import math


class Solution:
    def __init__(self):
        self.dataFilename = r"..\..\Data\input.dat"
        self.outputFilename = "output.txt"
        self.points = None
        self.validPoints = None
        self.readData()
        self.filterPoints()
        self.record()

    def readData(self):
        with open(self.dataFilename, 'rb') as file:
            rawData = file.read()
            self.points = [(int.from_bytes(rawData[i:i + 4], byteorder='big', signed=True),
                            int.from_bytes(rawData[i + 4:i + 8], byteorder='big', signed=True))
                           for i in range(len(rawData))[::4]]

    def filterPoints(self):
        self.validPoints = [point for point in self.points if point[0] > 0 and point[1] > 0]

    def record(self):
        point = tuple(map(int, input("请输入坐标点，逗号分隔：").split(',')))
        k = eval(input("请输入k："))
        results = list(zip(self.validPoints, (Solution.calDis(p, point) for p in self.validPoints)))
        results.sort(key=lambda x: x[1])
        with open(self.outputFilename, "w") as file:
            for item in results[:k]:
                file.write("point={} dis={:.2f}\n".format(item[0], item[1]))

    @staticmethod
    def calDis(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == "__main__":
    solution = Solution()
