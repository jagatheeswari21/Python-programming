n1=int(raw_input())
import random
min = 1
max = 4
max1 = 6
max2 = 12
max3 = 18
  
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
  print "Rolling the dices..."
  print "The values are...."
  if(n1==4):
    print random.randint(min, max)
      
    roll_again = raw_input("Roll the dices again?")
  elif(n1==6):
    print random.randint(min, max1)

    roll_again = raw_input("Roll the dices again?")
  elif(n1==12):
    print random.randint(min, max2)

    roll_again = raw_input("Roll the dices again?")
  elif(n1==18):
    print random.randint(min, max3)

    roll_again = raw_input("Roll the dices again?")
  else:
    print "invalid"
    

  
