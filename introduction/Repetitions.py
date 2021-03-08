str = input()
arr = list(str)
m=-1
s = set()
for i in range(len(arr)):
    c=1
    if arr[i]==arr[i-1] and i>=1:
        continue
    for j in range(i+1,len(arr)):
        if arr[j]==arr[i]:
            c+=1
        else:
            break
    if c>m:
        m=c
print(m)