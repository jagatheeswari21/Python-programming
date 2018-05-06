num=int(raw_input())
a=1
b=0
for series in range(0,num):
 a, b = b, a + b
 print b
