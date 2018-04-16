num=int(raw_input())
array=raw_input().split()
array=map(int,array)
if(num==len(array)):
  for i in array:
    ans1=min(array)
    ans2=max(array)
  print ans1,ans2  
else:
  print 'error'
