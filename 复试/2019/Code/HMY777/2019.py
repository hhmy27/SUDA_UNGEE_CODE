import math
class Solution(object):
    def __init__(self):
        self.arr = []
        self.res = [0] * 10
        self.path = '../../Data/Data.txt'
        self.d = {}  # 存放一个数和它的因子和的字典

        self.read_file()
        self.print()
        self.count()
        self.print_res()
        self.sort_array()
        self.filter_array()
        self.write_file()

    def read_file(self):
        # 读取文件中的数据，按文件中顺序存放在arr中
        with open(self.path) as fb:
            for line in fb:
                self.arr.append(int(line.strip()))  # 读文件，存放int数据

    def print(self):
        # 将arr中的内容显示在屏幕上，每行10个数，每个整数占6列
        print("print的结果:")
        for i in range(len(self.arr)):
            print("{:6}".format(self.arr[i]), end=' ')
            if (i + 1) % 10 == 0:
                print()

    def count(self):
        # 统计0~9在arr中所有整数中出现的次数，并存放到res中
        for num in self.arr:
            s = str(num)
            for ch in s:
                self.res[ord(ch) - ord('0')] += 1

    def print_res(self):
        # 将res输出，每行5个元素，可复用print()
        print("print_res 的结果:")
        for i, time in enumerate(self.res):
            print("{:}出现了{:}次".format(i, time))

    def sort_array(self):
        # arr中的整数按因子和升序排列，因子和相等的则按原大小排列（1和其本身也是因子）
        # 一个数的因子是它的因子数，一个数的因子和等于它的因子数+1+本身
        # 8->1 2 4 8 = 15
        # 9 -> 1 3 3 9 = 16
        # 10 -> 1 2 5 10 = 18
        # 12 -> 1 2 6 12 = 21
        # factor求一个数的因子和
        def factor(num):
            t = num
            ans = []
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    ans.append(i)
                    num /= i
            if num != 1:
                ans.append(num)
            ans.append(t)
            return int(sum(ans))

        for num in self.arr:
            self.d[num] = factor(num)
        # 对字典按照value排序，value相同的不改变位置，返回一个元组列表
        sortlist = sorted(self.d.items(), key=lambda item: item[1])
        self.d.clear()
        for item in sortlist:
            self.d.setdefault(item[0], item[1])

    def filter_array(self):
        # 对arr进行筛选，将偶数筛选出来放在头部，其他的放在后面。若使用辅助数组扣10分
        ind = 0  # 记录偶数的下标
        i = 0  # 遍历arr
        for i in range(len(self.arr)):
            if self.arr[i] % 2 == 0:
                self.arr[i], self.arr[ind] = self.arr[ind], self.arr[i]
                ind += 1

    def write_file(self):
        # 将偶数分解成质数，每个数占一行写到output.txt中
        # 任何一个大于等于4的偶数都能被分解成两个质数
        def is_prime(num):  # 判断质数
            if num == 2:
                return True
            if num == 0 or num == 1:
                return False
            if num % 2 == 0:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i == 0):
                    return False
            return True

        L = []
        for num in self.arr:
            if (num % 2 != 0):
                continue
            # 找到偶数了
            lst=[]
            tnum=num
            for i in range(2,num):
                while(num%i==0):
                    lst.append(str(i))
                    num/=i
            L.append((tnum,lst))
        with open('output.txt', 'w') as fb:
            for item in L:
                fb.write('{:} : {:}\n'.format(item[0], '*'.join(item[1])))


if __name__ == '__main__':
    solution = Solution()

