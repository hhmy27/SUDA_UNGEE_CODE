import random

if __name__ == '__main__':
    with open('input.dat', 'wb') as fb:
        for i in range(200):
            num = random.randint(-100, 100)
            print(num, end=' ')
            fb.write(num.to_bytes(4, byteorder="big", signed=True))
