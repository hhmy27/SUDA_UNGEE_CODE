import random

if __name__ == '__main__':
    """    
    说明
    @k : 5~10 以内的随机数
    @dimension : 2~5 以内的随机数，表示坐标的维度
    
    1.写入k和dimension
    2.写入50个坐标点，坐标值为 0~100 以内的随机数
    3.按照空格分隔数据
    """
    k = random.randint(5, 10)
    dimension = random.randint(2, 5)
    with open('data.txt', 'w') as fb:
        fb.write("{:} ".format(k))
        fb.write("{:} ".format(dimension))
        L = [random.randint(0, 100) for i in range(50 * dimension)]
        fb.write(' '.join(map(str, L)))

