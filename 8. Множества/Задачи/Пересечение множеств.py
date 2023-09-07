"""
a = set(map(int, input().split()))
b = set(map(int, input().split()))
i =a.intersection(b)
print(i)
"""
print(set(map(int, input().split())).intersection(set(map(int, input().split()))))