n1,n2,n3=raw_input().split(' ')
if(int(n1)>=int(n2) and int(n1)>=int(n3)):
  print n1
elif(int(n2)>=int(n1) and int(n2)>=int(n3)):
  print n2
else:
  print n3
