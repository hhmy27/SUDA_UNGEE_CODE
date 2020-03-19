import random

if __name__ == '__main__':
    # 写入了200个[-30,30]的坐标点
    with open('input.dat','wb') as fb:
        for i in range(200):
            num = random.randint(-30,30)
            fb.write(num.to_bytes(4, byteorder='big', signed=True))
