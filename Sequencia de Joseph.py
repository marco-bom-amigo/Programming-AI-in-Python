def seq_joseph(max_num):
    a = 0
    for i in range(max_num):
        mod = i % 2
        if mod != 0:
            a = i**2
            yield a

for x in seq_joseph(10):
    print(x)