from math import sqrt
if __name__ == '__main__':
    # 找出100~1000中不含9的素数，将结果输入到result文件中
    n=1000
    L = [i for i in range(100, n + 1) if 0 not in [i % j for j in range(2, int(sqrt(i)) + 1)]]
    with open("result.txt",'w') as fb:
        fb.write(str(L))