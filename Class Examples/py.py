#φ(n) = (p - 1) * (q - 1)
from tkinter import N
from Crypto.Util.number import bytes_to_long, long_to_bytes, str2long
p = 24211679580195880841
q = 98641300066272861769
e = 65537
m = "asodfijosidf"
mname = 276334567433
# noo = bytes_to_long("asodfijosidf")
t = (p-1) * (q-1)
n = p * q
d = pow(e, -1, t)
print(t)
print(d)
# m = 97115111100102105106111115105100102
# c = (noo**e) % n 
m = bytes(m, "utf-8")
m = bytes_to_long(m)
# print(c)
c = pow(m, e, n)
print(c)