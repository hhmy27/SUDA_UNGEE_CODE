import re


class Solution:
    def __init__(self):
        self.dataFilename = r"..\..\Data\input.txt"
        self.outputFilename = "output.txt"
        self.words = None
        self.freqWords = None
        self.statistics = {}
        self.readWords()
        self.sort()
        self.record()

    def readWords(self):
        cache = []
        patter = re.compile("^\s$")
        with open(self.dataFilename) as file:
            while True:
                c = file.read(1)
                if c == '':
                    break
                elif re.fullmatch(patter, c):
                    if len(cache) != 0:
                        word = "".join(cache)
                        cache.clear()
                        self.statistics[word] = self.statistics.get(word, 0) + 1
                else:
                    cache.append(c)

    def sort(self):
        self.freqWords = sorted((item for item in self.statistics.items() if item[1] > 5), key=lambda x: x[1], reverse=True)

    def record(self):
        with open(self.outputFilename, "w") as file:
            for item in self.freqWords:
                file.write("%s : %d\n" % (item[0], item[1]))


if __name__ == "__main__":
    solution = Solution()