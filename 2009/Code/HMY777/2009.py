import re
class Solution(object):
    def __init__(self):
        self.strLst=[]
        self.numLst=[]
        self.read_file()
        self.process_data()
        self.write_file()

    def read_file(self):
        path='../../Data/data.txt'
        with open(path) as fb:
            for line in fb:
                self.strLst.append(line.strip().split(','))
        for line in self.strLst:
            for i in range(len(line)):
                tstr = ''
                for ch in line[i]:
                    if(ch!=' '):
                        tstr+=ch
                line[i]=tstr
        print(self.strLst)

    def process_data(self):
        for line in self.strLst:    # 处理每一行
            tlst=[]
            num = 0
            for s in line:  # 处理每一行中的单个数字字符串
                if  s[0]!='0':
                    num=int(s)
                else:
                    num=int(s[1:],base=8)
                tlst.append(num)
                tlst.sort()
            self.numLst.append(tlst)

    def write_file(self):
        with open('./result.txt','w') as fb:
            for line in self.numLst:
                for num in line:
                    fb.write("{:} ".format(num))
                fb.write("\n")

if __name__ == '__main__':
    solution=Solution()
