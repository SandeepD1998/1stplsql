l = [14,4,35,10,7,15,20,49,62,63,45,70]
s = set( )
for i in l:
    if i%5 == 0 and i%7==0:
        s.add(i)
print(s)
def _sum(s):
    sum = 0
    for i in s:
        sum=sum + i
    return(sum)
ans =_sum(s)
print(ans)
s.remove(min(s))
print("deleting the lowest number: ",s)
