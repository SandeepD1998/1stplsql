# 2.Find how many numbers are divisible by 5 and 7
from itertools import count


a = [10,45,67,89,100,33,112,77,50,35,70,105,140,52,32,89,79,10,5]
#b=[]
#c=0
for i in a:
    if(i%5==0 and i%7==0):
        #c=c+1
        #b.append(i)
        print(i,end=" ")
#print(len(b))
#print(c)