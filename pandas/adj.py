import numpy as np

def letra_a():
    letra = np.zeros([4, 4])

    letra[1, 0] = 1
    letra[2, 0] = 1
    letra[3, 0] = 1

    letra[0, 1] = 1
    letra[2, 1] = 1

    letra[0, 2] = 1
    letra[2, 2] = 1

    letra[1, 3] = 1
    letra[2, 3] = 1
    letra[3, 3] = 1

    return letra

def letra_d():
    letra = np.zeros([4, 4])

    letra[0, 0] = 1
    letra[1, 0] = 1
    letra[2, 0] = 1
    letra[3, 0] = 1

    letra[0, 1] = 1
    letra[3, 1] = 1

    letra[0, 2] = 1
    letra[3, 2] = 1

    letra[1, 3] = 1
    letra[2, 3] = 1

    return letra

def letra_j():
    letra = np.zeros([4,4])

    letra[0,0] = 1
    letra[2,0] = 1
    letra[3,0] = 1

    letra[0,1] = 1
    letra[3,1] = 1

    letra[0,2] = 1
    letra[1,2] = 1
    letra[2,2] = 1
    letra[3,2] = 1

    letra[0,3] = 1

    return letra

print(letra_a())
print(letra_d())
print(letra_j())

