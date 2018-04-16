num=int(raw_input())
array=raw_input().split()
array=map(int,array)
sum=0
if(num==len(array)):
  for i in array:
    sum=sum+i
    avg=sum/num
  print avg
else:
  print 'error'
