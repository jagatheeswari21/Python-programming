n1,n2=raw_input().split()
for n in range(int(n1)+1,int(n2)):
  a=len(str(n))
  sum=0
  temp=n
  while(temp>0):
    dig=temp%10
    sum=sum+dig**a
    temp=temp/10
  if(n==sum):
    print n,
