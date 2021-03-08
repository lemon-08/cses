n = int(input())
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
else:
    if n%2==0:
        print(n//2,end=" ")
        for i in range(n//2):
            if i==n//2-1:
                print(n-i,end=" ")
            else:
                print(n-i,i+1,end=" ")
    else:
        print(n//2+1,end=" ")
        for i in range(n//2):
            print(n-i,i+1,end=" ")

    