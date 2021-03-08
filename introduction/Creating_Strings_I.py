from itertools import permutations 
arr = input()
li = sorted(set(permutations(arr)))
print(len(li))
for i in li:
    print("".join(i))