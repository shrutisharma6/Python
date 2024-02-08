# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int , input().split()))

m = int(input())
B = set(map(int , input().split()))

s = A.difference(B)

print(len(s))
