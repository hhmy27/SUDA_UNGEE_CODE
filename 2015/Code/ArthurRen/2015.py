import math


class Solution:
    def __init__(self):
        self.dataFilename = r"..\..\Data\input.dat"
        self.outputFilename = "output.txt"
        self.points = None
        self.validPoints = None
        self.readData()
        self.getValidPoints()
        self.record()

    def readData(self):
        with open(self.dataFilename, "rb") as file:
            rawData = file.read()
            self.points = [(int.from_bytes(rawData[i:i + 4], byteorder='big', signed=True),
                            (int.from_bytes(rawData[i + 4:i + 8], byteorder='big', signed=True)))
                           for i in range(len(rawData))[::8]]

    def getValidPoints(self):
        self.validPoints = [point for point in self.points if point[0] > 0 and point[1] > 0]

    def record(self):
        k = eval(input("请输入k:"))
        n = eval(input("请输入n:"))
        points = []
        for i in range(len(self.validPoints)):
            for j in range(i + 1, len(self.validPoints)):
                dis = Solution.getDis(self.validPoints[i], self.validPoints[j])
                if dis < n:
                    points.append(((self.validPoints[i], self.validPoints[j]), dis))

        with open(self.outputFilename, "w", encoding="utf-8") as file:
            file.writelines("有效点有%d个\n" % (len(self.validPoints)))
            file.write("k = %d\n" % k)
            file.write("n = %d\n" % n)
            file.write("count = %d\n" % len(points))
            file.writelines("{}, dis = {:.2f}\n".format(item[0], item[1]) for item in points)

    @staticmethod
    def getDis(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == "__main__":
    solution = Solution()
