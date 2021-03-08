n = int(input())
s = (n*(n+1))//2
if s%2==0:
    print("YES")
    s=s//2
    #print(s)
    arr = [n-i for i in range(n)]
    arr1 = []
    arr2 = []
    for i in range(n):
        if arr[i]<=s:
            s-=arr[i]
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    print(len(arr1))
    print(" ".join(map(str,arr1)))
    print(len(arr2))
    print(" ".join(map(str,arr2)))

else:
    print("NO")