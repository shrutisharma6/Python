n = int(input())
A = set(map(int, input().split()))
m = int(input())

for i in range(m):
    s = input().split()
    if s[0] == "intersection_update":
        B = set(map(int, input().split()))
        A.intersection_update(B)
    elif s[0] == "update":
        B = set(map(int, input().split()))
        A.update(B)
    elif s[0] == "symmetric_difference_update":
        B = set(map(int, input().split()))
        A.symmetric_difference_update(B)
    else:
        B = set(map(int, input().split()))
        A.difference_update(B)

print(sum(A))