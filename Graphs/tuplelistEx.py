
#tuple (immutable)
x = ('a', 'b', 'c')
print(x[1:])
value1, *value2 = x
print(value1)
print(value2)
#list (mutable)
bikes = ['z', 't', 'c', 'r', 's']
bikes[1] = 'hi'
bikes.append('bye')
bikes.insert(2, 'com')
print(bikes)

del bikes[2]
print(bikes.pop()) #remomve the last
print(bikes.pop(0)) #remove the first
bikes.sort()
print(bikes)

testing = [1, 2, 3, 4, 5]
print(testing[3:0:-1])
print(testing[:4])
print(testing[-3:])