a = [10,-233,45,-188,56,29,100,22,119,112,190,-144]

neg = []
for i in a:
    if (i<0):
        neg.append(i)
print("negative numbers are:" ,len(neg),'\n',neg)
for k in a:
    if k==112:
        a.remove(112)
        print("The number",k,"is removed",'\n',a)