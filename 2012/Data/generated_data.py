import random
import pickle
if __name__ == '__main__':
    # 写入了200个[-30,30]的坐标点
    with open('input.dat','wb') as fb:
        for i in range(200):
            pickle.dump(random.randint(-30,30),fb)
