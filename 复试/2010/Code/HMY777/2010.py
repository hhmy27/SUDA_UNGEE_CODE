class Solution(object):
    def __init__(self):
        self.numLst=[]
        self.read_file()
        self.maxNum=0
        self.minNum=0
        self.maxPrime=0
        self.midMinNum=0
        self.midMaxNum=0
        self.read_file()
        self.process_data()
        self.write_file()

    def read_file(self):
        path='../../Data/data.txt'
        with open(path) as fb:
            for line in fb:
                self.numLst.append(int(line.strip()))

    def process_data(self):
        self.numLst.sort()
        self.minNum=self.numLst[0]
        self.maxNum=self.numLst[-1]
        for num in self.numLst[::-1]:
            if self.is_prime(num) :
                self.maxPrime=num
                break
        self.midMinNum=self.numLst[len(self.numLst)//3]
        self.midMaxNum=self.numLst[len(self.numLst)//3*2]

    def is_prime(self,num):
        if num==2:
            return True
        if num==0 or num==1:
            return False
        if num%2==0:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

    def write_file(self):
        with open('output.txt','w') as fb:
            fb.write("min: {:}, max: {:}\n".format(self.minNum,self.maxNum))
            fb.write("max prime: {:}\n".format(self.maxPrime))
            fb.write("mid min: {:},mid max: {:}".format(self.midMinNum,self.midMaxNum))
if __name__ == '__main__':
    solution=Solution()
