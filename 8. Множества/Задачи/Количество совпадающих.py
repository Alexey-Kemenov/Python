"""
a = set(map(int, input().split()))
b = set(map(int, input().split()))
u = a.intersection(b)
print(len(u))
"""
print(len(set(map(int, input().split())).intersection(set(map(int, input().split())))))
