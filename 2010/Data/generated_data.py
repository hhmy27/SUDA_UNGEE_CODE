import random
if __name__ == '__main__':
    # 写入了200个[-30,30]的坐标点
    with open('data.txt','w') as fb:
        for i in range(2048):
            fb.write("{:}\n".format(random.randint(0,2048)))