import random
import pickle
if __name__ == '__main__':
    with open('./data.bin','wb') as fb:
        for i in range(100):
            a=random.randint(0,20)
            pickle.dump(a,fb)



