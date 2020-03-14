import pickle
# 从网页上下载input.dat文件，这里面是用二进制编写的，里面放了一堆int类型的数，每个数占4个字节，每次读取两个，这两个数构成一个坐标。
# 规定处以第一象限的数是有效点（x > 0&&y > 0）,问共有 多少个有效点。
# 现用户从键盘输入一个左边和数字k，输出k个离该点最近的点的坐标和每个坐标到该点的距离，写入output.txt中。
class Solution(object ):
    def __init__(self):
        self.points=[]
        self.validPoints=[]
        self.read_file()
        self.select_vaild_points()
        self.func((5,5),5)
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

    def func(self,points,k):
        ansList=[]
        for i in range(len(self.validPoints)):
            ansList.append((self.validPoints[i],self.distance(self.validPoints[i],points)))
        ansList.sort(key= lambda item:item[1])
        # print(ansList[:k])
        with open('./output.txt', 'a') as fb:
            for item in ansList[:k]:
                fb.write(str(item[0])+'\n')

    def distance(self,p1,p2):
        return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

if __name__ == '__main__':
    solution=Solution()
    pass