def power(base,exp,mod):
    ans = 1
    for _ in range(exp):
        ans = ans*base % mod 
    return ans
n = int(input())
t=10**9+7
print(power(2,n,t))