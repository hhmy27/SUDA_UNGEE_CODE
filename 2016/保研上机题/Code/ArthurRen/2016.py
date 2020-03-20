import os.path as path


class Solution:
    def __init__(self):
        self.dataDir = r"..\..\Data"
        self.inputFilename = path.join(self.dataDir, "input.txt")
        self.wordsFilename = path.join(self.dataDir, "words.txt")
        self.outputFilename = "output.txt"
        self.encoding = "utf-8"
        self.words = None
        self.article = None
        self.maxWordLength = None
        self.readData()
        self.segmentWord()

    def readData(self):
        with open(self.inputFilename, encoding=self.encoding) as file:
            lines = file.readlines()
            print(lines[0], lines[-1], end="\n")
            self.article = "".join(lines)

        with open(self.wordsFilename, encoding=self.encoding) as file:
            file.readline()
            lines = [line.strip() for line in file.readlines()]
            print(" ".join(lines[-3:]))
            self.words = set(lines)
            self.maxWordLength = max(len(word) for word in self.words)

    def segmentWord(self):
        with open(self.outputFilename, "w", encoding=self.encoding) as file:
            leftChars = ""
            startPos = 0
            while True:
                endPos = startPos + self.maxWordLength - len(leftChars)
                word = leftChars + self.article[startPos: endPos]
                if word == "":
                    return
                word, leftChars = self.matchWord(word)
                file.write(word + " ")
                startPos = endPos

    def matchWord(self, word) -> (str, str):
        left = ""
        while True:
            if word in self.words:
                return word, left
            else:
                left = word[-1] + left
                word = word[:-1]
                if len(word) == 1:
                    return word, left


if __name__ == "__main__":
    Solution()
