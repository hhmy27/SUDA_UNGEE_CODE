import random

if __name__ == '__main__':
    with open('./data.bin', 'wb') as fb:
        for i in range(100):
            a = random.randint(0, 35)
            fb.write(a.to_bytes(1, byteorder='big', signed=False))