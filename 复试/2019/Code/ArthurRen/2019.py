import math
from typing import List


class Solution:

    def __init__(self):
        self.dataFilename = "../../Data/Data.txt"
        self.outputFilename = "output.txt"
        self.arr = []
        self.res = [0 for _ in range(10)]
        self.primeGenerator = Solution.findNextPrime()
        self.debug = False
        self.primes = []
        self.read_file()
        self.print()
        self.count()
        self.print_res()
        self.sort_array()
        self.filter_array()
        self.write_file()

    def read_file(self):
        """
        将 "../../Data/Data.txt" 文件下的所有数字读入 arr 数组中
        """
        with open(self.dataFilename) as file:
            self.arr.extend((int(line.rstrip("\n")) for line in file))

    def print(self):
        """
        打印 arr 数组中的数字
        """
        if self.debug:
            print("arr:")
        Solution.printList(self.arr, 10)

    def count(self):
        """
        计算 0 ~ 9 在 arr 每个数字中出现的次数，并村放入 res 数组中
        """
        for i in self.arr:
            while i != 0:
                self.res[i % 10] += 1
                i //= 10

    def print_res(self):
        """
        打印 res 数组
        """
        if self.debug:
            print("res:")
        Solution.printList(["%d:%d" % (i, self.res[i]) for i in range(len(self.res))], 5)

    def sort_array(self):
        """
        对 arr 数字中的数字按照因数和的升序排序
        """
        factorsSums = (Solution.getFactorsSum(i) for i in self.arr)
        zip_array = [x for x in zip(self.arr, factorsSums)]
        zip_array.sort(key=lambda x: x[1])
        self.arr = [i[0] for i in zip_array]
        if self.debug:
            print("sorted arr:")
            Solution.printList(self.arr, 10)

    def filter_array(self):
        """
        将 arr 中的偶数移动到数组的前半部分，奇数移动到后半部分
        使用快排的思想：从前往后找奇数，从后往前找偶数，然后交换位置
        """
        size = len(self.arr)
        i, j = 0, size - 1
        while i != j:
            while i != j and i < size and self.arr[i] % 2 == 0:
                i += 1
            if not (i != j and i < size):
                break
            while i != j and j >= 0 and self.arr[j] % 2 == 1:
                j -= 1
            if not (i != j and j >= 0):
                break

            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        if self.debug:
            print("filtered arr:")
            Solution.printList(self.arr, 10)

    def write_file(self):
        """
        对 arr 数组中的偶数进行质因数分解，并写入 output.txt 文件内
        """
        with open(self.outputFilename, "w") as file:
            for i in self.arr:
                if i % 2 == 0:
                    primes = Solution.divIntoPrimes(i, self.primes, self.primeGenerator)
                    file.write("%d = %s\n" % (i, "*".join(map(str, primes))))

    # <editor-fold desc="static method">\
    @staticmethod
    def printList(lst: List, cols: int):
        for i in range(len(lst))[::cols]:
            print(" ".join("{:6}".format(x) for x in lst[i:i + cols]))

    @staticmethod
    def getFactorsSum(num: int) -> int:
        if num == 1:
            return 1
        sum = 1 + num
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum

    @staticmethod
    def isPrime(num: int) -> bool:
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        limit = math.ceil(math.sqrt(num)) + 1
        for i in range(2, limit):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def findNextPrime():
        tick = 2
        while True:
            if Solution.isPrime(tick):
                # Use 'yield' to generate prime,
                # because we don't know the upper limit,
                # and we need to save the prime generated last time in order to save time
                yield tick
            tick += 1

    @staticmethod
    def divIntoPrimes(num: int, primes: List[int], primeGenerator) -> List[int]:
        results = []
        primesIterator = iter(primes)
        while num != 1:
            try:
                prime = next(primesIterator)
            except StopIteration:
                # All the found primes cannot be used to divide the number,
                # so we need to find new prime
                break
            while True:
                if num % prime == 0:
                    results.append(prime)
                    num //= prime
                else:
                    break

        # If the num is still not divided
        while num != 1:
            # Find the next new prime
            prime = next(primeGenerator)
            # Add the new prime to the found primes list
            primes.append(prime)
            # Keep looping until the new prime cannot div the num
            while True:
                if num % prime == 0:
                    results.append(prime)
                    num //= prime
                else:
                    break

        return results
    # </editor-fold>


if __name__ == "__main__":
    s = Solution()
