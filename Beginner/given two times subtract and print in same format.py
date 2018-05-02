hour1,mins1=raw_input().split()
hour2,mins2=raw_input().split()
if int(hour1)>int(hour2)and(mins1>=mins2):
  hour=int(hour1)-int(hour2) 
  mins=int(mins1)-int(mins2)
  print hour,mins
elif int(hour1)<int(hour2)and(mins1<=mins2):
  hour=int(hour2)-int(hour1)
  mins=int(mins2)-int(mins1)
  print hour,mins
else:
  print 'error'
