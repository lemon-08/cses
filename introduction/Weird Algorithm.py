n = int(input())
s = set()
while True:
    if n==1:
        print(1)
        break
    if n in s:
        break
    else:
        s.add(n)
        print(n,end=" ")
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
