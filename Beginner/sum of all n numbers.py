num=int(raw_input())
results=raw_input().split()
results = map(int, results)
sum=0
if(num==len(results)):
  for x in results:
    sum=sum+x
  print sum 
else:
  print 'error'
