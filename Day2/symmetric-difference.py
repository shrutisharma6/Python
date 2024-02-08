# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
M_set = set(map(int, input().split()))
n = int(input())
N_set = set(map(int, input().split()))
ans=list((M_set.difference(N_set)).union(N_set.difference(M_set)))
ans.sort()
for i in ans:
    print(i)
