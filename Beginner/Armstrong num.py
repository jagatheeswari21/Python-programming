num=int(raw_input())
a=len(str(num))
temp=num
sum=0
while(num>0):
  dig=num%10
  sum=sum+dig**a
  num=num/10
if (temp==sum):
  print "yes"
else:
  print "no"
