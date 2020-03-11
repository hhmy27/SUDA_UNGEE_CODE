import random
if __name__ == '__main__':
    with open('Data.txt','w') as fb:
        L=[random.randint(0,32768) for i in range(100)]
        for num in L:
            fb.write(str(num)+'\n')