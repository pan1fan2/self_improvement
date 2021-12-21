#itertools : product,permuations,combinations,accumulate,groupby,and infinite iterators

from itertools import groupby, permutations, product,combinations,accumulate
a = [1,2]
b = [3,4]
prod = product(a,b) 
#print(list(prod)) #[(1, 3), (1, 4), (2, 3), (2, 4)]

a = [1,2,3]
perm = permutations(a)
#print(list(perm)) #(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm = permutations(a,2)
# print(list(perm)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

comb = combinations(a,2)
#print(list(comb)) #[(1, 2), (1, 3), (2, 3)]

acc = accumulate(a)
#print(list(acc))#[1, 3, 6] = [1, 1+2, 1+2+3]
import operator
acc = accumulate(a,func = operator.mul)
#print(list(acc)) #[1, 2, 6]

#比较大小，然后保留最大
a = [1,2,5,3,4]
acc = accumulate(a,func = max)
#print(a) #[1, 2, 5, 3, 4]
#print(list(acc))#[1, 2, 5, 5, 5]

# 按所给条件分组
from itertools import groupby
# def smaller_than_3(x):
#     return x < 3
# a = [1,2,3,4]
# group_obj = groupby(a,key=smaller_than_3)
# group_obj = groupby(a,key=lambda x : x < 3)
# for key,value in group_obj:
    #print(key,list(value))
# True [1, 2] 1和2 are groupec together
# False [3, 4]

# eg2
# persons = [{'name':'Tim','age':25},{'name':'Dan','age':25},{'name':'Lisa','age':27},{'name':'Claire','age':28}]
# group_obj = groupby(persons,key=lambda x :x['age'])
# for key,value in group_obj:
#     print(key, list(value))

# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]


