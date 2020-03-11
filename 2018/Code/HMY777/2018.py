class Solution(object):
    def __init__(self):
        self.num_list = []
        self.max_num_list = []
        self.read_file()
        self.selete_prime()
        self.selete_rest_num()
        self.write_file()

    def read_file(self):
        # 读入文件，存入num_list
        with open('../../Data/Data.txt') as fb:
            for line in fb:
                self.num_list.append(int(line))

    def write_file(self):
        with open('output.txt', 'w') as fb:
            fb.write(str(len(self.max_num_list)) + '\n')
            for i in range(len(self.max_num_list)):
                fb.write("{:>4}".format(self.max_num_list[i]))
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
        for num in self.num_list:
            if self.is_prime(num):
                self.max_num_list.append(num)

    def selete_rest_num(self):
        for num in self.num_list:
            if num in self.max_num_list:
                continue
            flag = True
            for prime in self.max_num_list:
                if self.gcd(num, prime) != 1:
                    flag = False
                    break
            if flag:
                self.max_num_list.append(num)


if __name__ == '__main__':
    solution = Solution()
