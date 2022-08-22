from math import sqrt

# lenh for
'''gt = 1
for x in range(1, 10):
    gt *= x

print(gt)
'''
#
# 
''' 
n = int(input("Nhap n = "))
gt = 1
for x in range(1, n + 1):
    gt *= x

print(gt)
'''
'''n = int(input("Nhap n = "))
s = 0
for x in range(1, n + 1):
    s += x * (n + 1 - x)

print(s)'''

# Ham zip
'''a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = list(zip(a,b,a[::-1]))

print(c)'''


'''n = int(input())
a = list(range(1, n + 1))
s = 0
for x, y in zip(a, a[:-1]): 
    s += x * y
print(s)'''


# Kiem tra so nguyen to
'''n = int(input())
m = int(sqrt(n))
ok = True
for i in range (2, m + 1):
    if n % i == 0:
        ok = False
        break
print("yes" if ok and n > 1 else "no")'''
