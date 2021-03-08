li = [[1,2,9,25],[4,3,8,11,24],[5,6,7,12,23],[16,15,14,13,12,22],[17,18,19,20,21]]       
for _ in range(int(input())):
    n,m = map(int,input().split())
    print(li[n-1][m-1])