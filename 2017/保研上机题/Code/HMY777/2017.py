import matplotlib.pyplot as plt


class Solution(object):
    def __init__(self):
        self.path = '../../Data/data.txt'
        self.k = 0
        self.dimension = 0
        self.num_list = []  # 存放读入的数字
        self.points = []  # 存放根据数据产生的点
        self.min_points = tuple()  # 存放最近的两个点
        self.min_distance = 0  # 存放所有点中最小的距离
        self.min_point_distance_dict = dict()  # 存放所有点到最近点的距离的字典

        self.read_file()
        self.generate_points()
        self.cal_min_distance_point()
        self.cal_distance_with_min_point()
        self.find_k_points()
        # self.draw_points()

    def read_file(self):
        # 读文件
        with open(self.path) as fb:
            L = fb.read().split()
            L = list(map(eval, L))
            # print(L)
            self.k = L[0]
            self.dimension = L[1]
            self.num_list = L[2:]
            # print(L)

    def generate_points(self):
        # 生成点
        for i in range(0, len(self.num_list), self.dimension):
            self.points.append(tuple(self.num_list[i:i + self.dimension]))

    # def draw_points(self):
    #     # 测试用，绘图
    #     plt.scatter([self.points[i][0] for i in range(len(self.points))],[self.points[i][1] for i in range(len(self.points))])
    #     plt.show()

    def cal_distance(self, p1, p2):
        # 计算距离
        return sum(((i[0] - i[1]) ** 2 for i in zip(p1, p2))) ** 0.5

    def cal_min_distance_point(self):
        # 默认最短距离是两个点
        self.min_distance = self.cal_distance(self.points[0], self.points[1])
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                # 计算两个点之间的距离
                distance = self.cal_distance(self.points[i], self.points[j])
                if distance < self.min_distance:
                    self.min_distance = distance
                    self.min_points = (self.points[i], self.points[j])
        print("距离最近的两个点是：{:},距离是{:}".format(self.min_points, self.min_distance))

    def cal_distance_with_min_point(self):
        # 计算所有点到两个最小点的距离
        for point in self.points:
            if point == self.min_points[0] or point == self.min_points[1]:
                continue
            min_distance = min(self.cal_distance(self.min_points[0], point),
                               self.cal_distance(self.min_points[1], point))
            self.min_point_distance_dict[point] = min_distance

    def find_k_points(self):
        md = sorted(self.min_point_distance_dict.items(), key=lambda item: item[1])
        print("距离最近的k个点是:", md[:self.k])


if __name__ == '__main__':
    solution = Solution()
