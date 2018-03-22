n1,n2=raw_input().split()
a=[]
for n in range(int(n1)+1,int(n2)):
  if(n%2==1):
    a.append(n)
for i in a:
  print i,
