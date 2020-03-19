import re


class Solution:
    def __init__(self):
        self.pathsFilename = r"..\..\Data\PathInput_2013.txt"
        self.requestFilename = r"..\..\Data\PathRequest_2013.txt"
        self.outputFilename = r"output.txt"
        self.pattern = re.compile("^\[[A-Z,\s0-9]*\]$")
        self.paths = []
        self.requests = []

        self.readData()
        self.process()

    def readData(self):
        with open(self.pathsFilename) as file:
            self.paths = [tuple(map(lambda x: x.strip(), line[1:-2].split(','))) for line in file if re.match(self.pattern, line)]

        with open(self.requestFilename) as file:
            self.requests = [tuple(map(lambda x: x.strip(), line[1:-2].split(','))) for line in file if re.match(self.pattern, line)]

    def process(self):
        with open(self.outputFilename, "w") as file:
            for request in self.requests:
                tick = int(request[2])
                success = self.__findPath(request[0], request[1], tick)
                file.write("[{}, {}]:{}\n".format(request[0], request[1], "YES" if success else "NO"))

    def __findPath(self, sp, dst, tick) -> bool:
        if tick == 0:
            return False
        else:
            matchPaths = [path for path in self.paths if path[0] == sp]
            for path in matchPaths:
                if path[1] == dst and tick == 1:
                    return True
                else:
                    if self.__findPath(path[1], dst, tick - 1):
                        return True
            else:
                return False


if __name__ == "__main__":
    solution = Solution()

