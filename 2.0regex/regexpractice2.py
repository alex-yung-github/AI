

import re

list = []
one = "can"
two = "man"
three = "fan"
list.append(one)
list.append(two)
list.append(three)
list.append("dan")
list.append("ran")
for str in list:
    print(re.findall("[cmf]an", str))

list2 = []
list2.append("bignum3923buteat")
list2.append("ilikepie")
list2.append("pie932")
list2.append("239adfiasdf")
list2.append("1")
list2.append("one1")
for str in list2:
    print(re.findall(".*[0-9]+.*", str))




