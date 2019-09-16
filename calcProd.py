#! python3

# 计算两次调用之间经过的时间

import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('the result is %s digits long.' % (len(str(prod))))
print('took %s second to calulate.' % (endTime - startTime))
