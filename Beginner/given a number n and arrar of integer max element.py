n=int(raw_input())
inputs=raw_input().split()
if(n==len(inputs)):
  inputs=map(int,inputs)
  print max(inputs)
else:
  print 'error'
