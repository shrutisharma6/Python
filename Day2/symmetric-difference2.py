n = int(input())
A = set(map(int , input().split()))

m = int(input())
B = set(map(int , input().split()))

s = A.symmetric_difference(B)

print(len(s))

