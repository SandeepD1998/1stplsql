a = [10,45,67,89,100,33,112,77,50,52,32,89,79,5]
r = []
for num in a:
    if (num % 2!=0):
        r.append(num)
print("odd numbers are present in a: ",len(r),'\n',r)
f = []
g = []
for i in a:
    if i%5==0:
        f.append(i)
    elif i%7==0:
        g.append(i)
s = len(f) + len(g)
h=f+g
print("Len of  Numbers which are divisible which are divisible by 5 and 7 :", s)
print(h)
print(a.sort())
print("Highest number:",a[-1])
print("Lowest number:",a[0])


