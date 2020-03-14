import pickle
class Solution(object):
    def __init__(self):
        self.vaildPoints=[]
        self.minPoint=None
        self.filterPoint=[]
        self.class_points=[]
        self.read_file()
        self.find_min_point()
        self.filter_point()
        self.classify_point()
        self.write_file()
        pass
    def read_file(self):
        path='../../Data/input.dat'
        nums=[]
        with open(path,'rb') as fb:
            while True:
                try:
                    nums.append(int(pickle.load(fb)))
                    # print(pickle.load(fb))
                except:
                    break
        for i in range(0,len(nums),2):
            if nums[i]>0 and nums[i+1]>0:
                self.vaildPoints.append((nums[i],nums[i+1]))    #放入有效点

    def find_min_point(self):
        self.minPoint=self.vaildPoints[0]
        for point in self.vaildPoints:
            if (point[0]*point[1])<(self.minPoint[0]*self.minPoint[1]):
                self.minPoint=point
        # print(self.minPoint)

    def filter_point(self):
        for point in self.vaildPoints:
            if point[0]>self.minPoint[0] and point[1]>self.minPoint[1]:
                if self._p1_greater_than_p2(point,self.minPoint):
                    self.filterPoint.append(point)
        # print(self.filterPoint)

    def classify_point(self):
        # 对有效点进行分组，每个有效点仅属于一个分组，组内：若对组内所有点的x进行排序，当x1 > x2时，y1 > y2
        # 思路:标记数组flag用于标记对应点是否已经被分类
        # ind是此次尝试分类的起点，也就是vaildPoints中第一个未被分类的点
        size=0
        ind=0
        flag=[0]*len(self.vaildPoints)
        tempVaildPoints=[]
        tempVaildPoints=list(sorted(self.vaildPoints))
        while size<len(tempVaildPoints):
            tlst=[]
            try:
                ind=flag.index(0)
            except:
                break
            tlst.append(tempVaildPoints[ind])
            flag[ind]=1
            lastPoint=tempVaildPoints[ind]
            for j in range(ind+1,len(tempVaildPoints)):
                if(not flag[j] and self._p1_greater_than_p2(tempVaildPoints[j],lastPoint)):
                    tlst.append(tempVaildPoints[j])
                    lastPoint=tempVaildPoints[j]
                    flag[j]=1
            self.class_points.append(tlst)

        # print(self.class_points)
        pass
    def _p1_greater_than_p2(self,p1,p2):
        if(p1[0]>p2[0] and p1[1]>p2[1]):
            return True
        return False
    def write_file(self):
        with open('./output.txt','w',encoding='UTF8') as fb:
            fb.write("最小矩形：{:}\n".format(self.minPoint[0]*self.minPoint[1]))
            fb.write("最小点: {:}\n".format(self.minPoint))
            fb.write("分组情况: {:}\n".format(self.class_points))
    pass

if __name__ == '__main__':
    solution=Solution()

    pass