from collections import Counter
a = "aaaaaabbbbcc"
my_counter = Counter(a)
# print(my_counter) #Counter({'a': 6, 'b': 4, 'c': 2})
# print(my_counter.most_common(1)) #[('a', 6)]  
# print(list(my_counter.elements())) #['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c']

# similar to a struct
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
#print(pt) #Point(x=1, y=-4)

# keep the input order
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 1
ordered_dict['c'] = 2
ordered_dict['d'] = 3
ordered_dict['a'] = 4
#print(ordered_dict) #OrderedDict([('b', 1), ('c', 2), ('d', 3), ('a', 4)])

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)#deque([1, 2])
d.appendleft(3)
print(d) #deque([3, 1, 2])
d.pop()
print(d) #deque([3, 1])
d.extend([4,5,6]) 
print(d) #deque([3, 1, 4, 5, 6])
d.rotate(1)
print(d) #deque([6, 3, 1, 4, 5])