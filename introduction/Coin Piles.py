for _ in range(int(input())):
    n,m = map(int,input().split())
    if n==m:
        if n%3==0:
            print("YES")
        else:
            print("NO")
    elif n==0 or m==0:
        print("NO")
    
    elif n//2>m or m//2>n:
        print("NO")
    else:
        if (m+n)%3==0:
            print("YES")
        else:
            print("NO")