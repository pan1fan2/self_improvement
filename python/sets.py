setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

#diff = setA.difference(setB) # {4, 5, 6, 7, 8, 9}

# returns all common elements from setA and setB 
#diff = setA.symmetric_difference(setB) # {4, 5, 6, 7, 8, 9, 10, 11, 12}
# print(diff)

# update set
#setA.update(setB) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# same as diff = setA.difference(setB)
#setA.difference_update(setB) # {4, 5, 6, 7, 8, 9}
#print(setA)

# relation
# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# setC = {7,8}
# print(setA.issuperset(setB)) #True
# print(setA.isdisjoint(setC)) #True

a = frozenset([1,2,3,4])
#a.add(2) #AttributeError: 'frozenset' object has no attribute 'add'
#a.remove(1) #AttributeError: 'frozenset' object has no attribute 'remove'
print(a)
