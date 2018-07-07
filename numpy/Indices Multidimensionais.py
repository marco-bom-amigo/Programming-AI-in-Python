import numpy as np

array_2d = np.array(( [ 1 ,2 ,3 ,4 ,5]
                    , [ 6 ,7 ,8 ,9,10]
                    , [11,12,13,14,15]
                    ))
print(array_2d)
print(array_2d[1])
print(array_2d[1][0])
print(array_2d[:2, 1:])

matriz = np.arange(20).reshape((4,5))
print(matriz)
print(matriz.T)

print(np.dot(matriz.T, matriz))

matriz_3d = np.arange(48).reshape((4,4,3))
print(matriz_3d)

array = np.array([[1,2,3,4]])
print(array)
print(array.swapaxes(0,1))
print(array.swapaxes(1,1))

array = np.arange(11)
array_random_1 = np.random.randn(4)
array_random_2 = np.random.randn(4)

print(array)
print(np.sqrt(array))
print(np.exp(array))

print("Add"     , np.add(     array_random_1, array_random_2))
print("Subtract", np.subtract(array_random_1, array_random_2))
print("Multiply", np.multiply(array_random_1, array_random_2))
print("Divide"  , np.divide(  array_random_1, array_random_2))
print("Power"   , np.power(   array_random_1, array_random_2))
print("Max"     , np.maximum( array_random_1, array_random_2))

print("Sin"   , np.sin(   array_random_1))
print("Cos"   , np.cos(   array_random_1))
print("Tan"   , np.tan(   array_random_1))
print("Arcsin", np.arcsin(array_random_1))

print("Arctan", np.arctan(array_random_1))

print("Greater"      , np.greater(array_random_1, array_random_2))
print("Greater equal", np.greater_equal(array_random_1, array_random_2))
print("Less"         , np.less(array_random_1, array_random_2))
print("Less equal"   , np.less_equal(array_random_1, array_random_2))