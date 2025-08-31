#find the minimum value in a list
l=list(map(int,input()))
minVal=l[0]
for i in l:
    if i<minVal :
        minVal = i
print(minVal)
