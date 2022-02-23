print("hellow world")

def f():
    global s
    print(s)
    s = "Updating the global variable"
    print(s)
s = "I Love Python"
f()
print(s)

edge = {0}
print(type(edge))

l = [123, 23, 43, 5, 56]
for i, j in enumerate(l):
    print(i, j)

