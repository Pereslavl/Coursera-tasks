v = int(input())
a = (v // 3600) % 24
b = v % 3600
d = b % 60
c = b // 60
if c < 10:
    c = "0" + str(c)
if d < 10:
    d = "0" + str(d)
    print(a, ":", c, ":", d, sep="")
