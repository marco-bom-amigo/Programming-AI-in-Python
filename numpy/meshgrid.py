import numpy as np
import matplotlib.pyplot as plt

pontos = np.arange(-5, 5, 1)
print(pontos)

array_1  = np.array([ 1,  2,  3,  4,  5,  6])
array_2  = np.array([31, 32, 33, 34, 35, 36])
condicao = np.array([True, False, True, False, True, False])
array_3 = np.where(condicao, array_1, array_2)
print(array_3)

array = np.random.randn(5,5)
print(array)
print(np.where(array < 0, 0, array))

px, py = np.meshgrid(pontos, pontos)
print(px)
print(py)

plt.plot( px
        , py
        , marker    = '.'
        , color     = 'k'
        , linestyle = 'none'
        )
plt.show()

