n = int(input())
t=5
ans=0
while True:
    if n//t<=0:
        break
    ans+=n//t 
    t*=5
print(ans)