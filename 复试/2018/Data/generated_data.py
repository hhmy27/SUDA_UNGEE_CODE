import random
if __name__ == '__main__':
    with open('Data.txt','w') as fb:
        L=[i for i in range(1,501) if i!=3 and i!=5 and i!=7]
        for num in L:
            fb.write(str(num)+'\n')