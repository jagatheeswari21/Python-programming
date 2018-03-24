n1,n2=raw_input().split()
for num in range(int(n1)+1,int(n2)):
   if num>1:
       for i in range(2,num):
           if (num%i)==0:
               break
       else:
           print num,
