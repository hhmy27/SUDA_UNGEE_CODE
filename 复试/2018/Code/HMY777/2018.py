from bisect import insort_left
class Solution(object):
    def __init__(self):
        self.numLst = []
        self.maxNumLst = []
        self.restNumLst={}
        self.read_file()
        self.selete_prime()
        self.selete_rest_num()
        self.write_file()

    def read_file(self):
        # 读入文件，存入num_list
        with open('../../Data/Data.txt') as fb:
            for line in fb:
                self.numLst.append(int(line))
        self.numLst.sort()

    def write_file(self):
        with open('output.txt', 'w') as fb:
            fb.write(str(len(self.maxNumLst)) + '\n')
            self.maxNumLst=list(set(self.maxNumLst))
            for i in range(len(self.maxNumLst)):
                fb.write("{:>4}".format(self.maxNumLst[i]))
                if (i + 1) % 5 == 0:
                    fb.write('\n')

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def is_prime(self, num):
        if num == 2: return True
        if num == 0 or num == 1: return False
        if num % 2 == 0: return False
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i == 0):
                return False
        return True

    def selete_prime(self):
        for i,num in enumerate(self.numLst):
            if self.is_prime(num):
                self.maxNumLst.append(num)
        self.restNumLst=list(set(self.numLst).difference(set(self.maxNumLst)))
        self.restNumLst.sort(reverse=True)      # restNumLst中的元素是非素数


    def selete_rest_num(self):
        # 开始遍历没有被选中的数据，尝试加入
        for n in self.restNumLst:
            iLst=[]
            for num in self.maxNumLst:
                if self.gcd(num,n)!=1:  # 找到了不互质的num
                    iLst.append(num)  #加入num
            if sum(iLst)>n:
                continue
            else :
                # 新加入的元素使得子集更大
                # 总是尝试加入最大的数，替换掉多个比当前数更小的数
                for i in iLst:
                    self.maxNumLst.remove(i)
                ind = len(self.maxNumLst)
                while ind > 0:
                    if (self.maxNumLst[ind - 1] < n):
                        break
                    ind -= 1
                self.maxNumLst.insert(ind,n)    # 在合适的位置插入，保持有序

if __name__ == '__main__':
    solution = Solution()
