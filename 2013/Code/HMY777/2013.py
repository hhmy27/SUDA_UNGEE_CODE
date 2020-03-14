class Solution(object):
    def __init__(self):
        self.road_map = [[]]
        self.road_dict = dict()
        self.size=0
        self.read_file_build_map()
        self.read_file_judge()
        pass

    def read_file_build_map(self):
        path = '../../Data/PathInput_2013.txt'
        with open(path) as fb:
            ind = 0
            road_list = []
            size = int(fb.readline().strip())
            for line in fb:
                # 读取到一条机场路径
                lst = line.strip('[]\n').split(', ')
                road_list.append(lst)
            for road in road_list:
                for name in road:
                    # print(name)
                    if name not in self.road_dict:
                        self.road_dict[name] = ind  # 存放一个机场的编号
                        ind += 1
            self.road_map = [[0 for i in range(ind)] for i in range(ind)]  # 用[0]*ind会导致所有的列表同时被修改
            self.size=ind
            for road in road_list:
                self.road_map[self.road_dict[road[0]]][self.road_dict[road[1]]] = 1  # 标记一条路径，路径是单向的

    def read_file_judge(self):
        path = '../../Data/PathRequest_2013.txt'
        with open(path) as fb,open('output.txt','w') as resultfb:
            size = int(fb.readline().strip())
            for request in fb:
                re = request.strip('[]\n').split(', ')
                start, end, num = self.road_dict[re[0]], self.road_dict[re[1]], int(re[2])
                mins=self.dijkstra(start,end)
                if mins<=num:
                    resultfb.write("YES\n")
                else:
                    resultfb.write("NO\n")
        pass

    def dijkstra(self,start,end):
        vis = [0] * self.size
        dis = [9999] * self.size
        dis[start]=0
        for i in range(self.size):
            u,MIN=-1,9999   #每轮找一个最近的点
            for j in range(self.size):
                if not vis[j] and dis[j]<MIN:
                    u,MIN=j,dis[j]
            if u==-1:
                return dis[end]
            vis[u]=True
            for v in range(self.size):  #更新坐标点
                if not vis[v] and self.road_map[u][v]!=0 and self.road_map[u][v]+dis[u]<dis[v]:
                    dis[v]=self.road_map[u][v]+dis[u]
        return dis[end]


if __name__ == '__main__':
    solution = Solution()
