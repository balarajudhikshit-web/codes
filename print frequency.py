a=input().split(",")
b=[]
for i in range(0,len(a),2):
    for j in range(int(a[i])):
        b+=[int(a[i+1])]


print(b)