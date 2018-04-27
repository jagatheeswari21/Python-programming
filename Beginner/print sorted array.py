num=int(raw_input())
inputs=raw_input().split()
if(num==len(inputs)):
  inputs=map(int,inputs)
  ans=sorted(inputs)
  for answers in ans:
    print answers,
