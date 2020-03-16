import random
if __name__ == '__main__':
    # 写入了2048个整数，随机0~2048
    with open('data.txt','w') as fb:
        for i in range(2048):
            fb.write("{:}\n".format(random.randint(0,2048)))
            