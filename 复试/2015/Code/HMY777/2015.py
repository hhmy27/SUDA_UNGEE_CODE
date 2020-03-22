import math
import pickle
# - 从网页上下载input.dat文件，里面是用二进制编写的，里面放了一堆int型的数，每个数占4字节，每次读取两个，这两个数构成一个坐标。
# - 处于第一象限的坐标为有效点，问其中有多少个有效点。
# - 从键盘输入k和n，从第一问中的有效点中找出距离小于n，距离小于n的点的个数要大于k，将它们以文本格式输出到文件中。
class Solution(object ):
    def __init__(self):
        self.points=[]
        self.validPoints=[]
        self.read_file()
        self.select_vaild_points()
        self.func(5,5)
        pass
    def read_file(self):
        tlist=[]
        with open('../../Data/input.dat', 'rb') as fb:
            for i in range(200):
                tlist.append(pickle.load(fb))
        for i in range(len(tlist)-1):
            self.points.append((tlist[i],tlist[i+1]))
    def select_vaild_points(self):
        for point in self.points:
            if(point[0]>0 and point[1]>0):
                self.validPoints.append(point)
        with open('./output.txt','w') as fb:
            fb.write("valid points : {:}\n".format(len(self.validPoints)))
        pass

    def func(self,k,n):
        ansList=[]
        for i in range(len(self.validPoints)):
            for j in range(i+1,len(self.validPoints)):
                if(self.distance(self.validPoints[i],self.validPoints[j])>k):
                    ansList.append((self.validPoints[i],self.validPoints[j]))

        with open('./output.txt', 'a') as fb:
            for item in ansList:
                fb.write(str(item)+'\n')

    def distance(self,p1,p2):
        return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

if __name__ == '__main__':
    solution=Solution()
    pass