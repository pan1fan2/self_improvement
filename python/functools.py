from functools import reduce

a = [1,2,3,4]

#对于reduce func都是涉及两个变量
product_a = reduce(lambda x,y : x*y,a)
# print(product_a) #24