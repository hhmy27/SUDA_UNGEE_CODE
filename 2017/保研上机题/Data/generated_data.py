import random

if __name__ == '__main__':
    # 说明
    # k为10，维度是2维，每两个整数构成一个点
    # 写入k和dimension
    # 随机写入100个范围在0~50的整数，构成50个点
    # 按照空格分隔数据
    k = 10
    dimension = 2
    with open('data.txt', 'w') as fb:
        fb.write("{:} ".format(k))
        fb.write("{:} ".format(dimension))
        L=[]
        for i in range(100):
            L.append(random.randint(0, 100))
        for num in L:
            fb.write(str(num)+' ')
