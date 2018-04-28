n,k=raw_input().split()
array=raw_input().split()
if int(n)==len(array):
  array=map(int,array)
  list=array[0:int(k)]
  print sum(i for i in list)
