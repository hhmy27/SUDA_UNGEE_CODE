import pickle
import math
class Circle(object):
    # 圆的类，包含构成半径的两个点，其中一个为原点，记录原包含的坐标点数，返回密度
    # 计算半径，和面积函数
    def __init__(self,point1,point2):
        self.center_point=point1
        self.another_point=point2
        self.include_points=0
        self.r=self.cal_distance(self.another_point)
        self.area=self.cal_area()

    def cal_area(self):
        return 3.14*self.r*self.r
    def cal_distance(self,a): #计算距离
        return((a[0]-self.center_point[0])**2+(a[1]-self.center_point[1])**2)**0.5
    def cal_density(self):
        return self.include_points/self.cal_area()

class Solution(object):
    def __init__(self):
        self.points=[]
        self.circles=[]
        self.read_file()
        self.generate_circle()
        self.cal_points_in_circle()
        self.sort_circle()
        self.display_circle()

    def read_file(self):
        with open('../../Data/data.bin','rb') as fb:
            while True:
                try:
                    a,b=[pickle.load(fb) for i in range(2)]
                    self.points.append((int(a),int(b)))
                except:
                    break
        # print(self.points)

    def generate_circle(self):  # 产生圆
        size=len(self.points)
        for ind in range(0,size):
            p1=self.points[ind]
            p2=self.points[(ind+1)%size]
            # print(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5)
            # c=Circle(p1,p2)
            # print(c.r)
            self.circles.append(Circle(p1,p2))

        # for i in self.circles:
            # print(i.r)

    def cal_points_in_circle(self):
        for circle in self.circles:
            for point in self.points:
                if circle.cal_distance(point)<=circle.r :
                    circle.include_points+=1    # 这样一定会加上构成该圆半径的两个点，最后要减去
            circle.include_points-=2

    def sort_circle(self):
        self.circles.sort(key=lambda circle:circle.include_points,reverse=True)

    def display_circle(self):
        with open('output.txt','w') as fb:
            for circle in self.circles[0:5]:
                fb.write("({:},{:}){:>5}{:>7.2f}\n".format(circle.center_point,circle.another_point,
                                                      circle.include_points,circle.cal_density()))



if __name__ == '__main__':
    solution=Solution()
