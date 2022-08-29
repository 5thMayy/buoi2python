'''
a = input("xin moi cho biet quy danh: ")
print("xin chao", a)

n = int(input("nhap n = "))
print(n**3)

a,b = input().split()
a = float(a)
b = float(b)
print("Dien tich HCN", a*b)

a = list(input().split())
print(a)
print(*a)
print(*a, sep=" va ")
'''
import math

'''
a = [4,7,2,8]
a.sort()
print(*a)
a.sort(reverse=True)
print(*a)
a[::-1]
print(*a)
'''

#b2
#lenh for
'''
for x in range (10): print(x,end = "  ")
'''
#tinh giai thua n!
'''
n = int(input())
s = 1
for x in range(1, n+1): s*= x
print("n! = ",s)
'''
#nhap n tinh s=1*n + 2*(n-1) + ... + n*1
'''
n = int(input())
s = 0 
for i in range(1,n+1) : s+=i*(n+1-i)
print("s = ",s)
'''

#ham zip
'''
a = [1,2,3,4,5,6]
b = ['a','b','c']
c = list(zip(a,b,a[::-1]))
print(c)
'''

#s = 1*2+2*3+...+(n-1)*n
'''
n = int(input())
a = list(range(1,n+1))
s = 0
for x,y in zip(a,a[1:]): s+=x*y
print(s)

from math import sqrt
#kiem tra so nguyen to
n = int(input())
m = int(sqrt(n))
ok = True
for i in range(2,m+1):
    if n%i==0:
        ok=False
        break
print("yes" if ok and n>1 else "no")

#in ra day fibonaci
n=int(input())
F=2*[1]
for _ in range(n): F.append(F[-1]+F[-2])
print(*F[:n])


#nhap day so nguyen va tinh
#s1 tong binh phuong cac phan tu
#s2 tong nhung so chan

a = list(map(int,input().split()))
b = [x*x for x in a]
print(sum(b))
c = [x for x in a if x%2==0]
if c==[]: print("khong co so chan")
else:print("tong chan ",sum(c))

#s3=a1+(a1+a2)+(a1+a2+a3)+...+(a1+...an)
s=0
for i,x in enumerate(a): s+=sum(a[:i+1])
print(s)

#nhap day so nguyen kiem tra day co tang dan ko?a1<a2<...<an?
a=list(map(int,input().split()))
ok=True
for i in range(len(a)-1):  
    if a[i]>=a[i+1]:
        ok=False
        break
print("day tang" if ok else "khong phai day tang")


a=list(map(int,input().split()))
b = [1 for x,y in zip(a,a[1:]) if x>=y]
print("day tang" if b==[] else "khong phai day tang")

#kiem tra doi xung
a=list(map(int,input().split()))
print("doi xung" if a==a[::-1] else "ko doi xung")

#dem so bo 3 lien tiep tap cap so cong
a=list(map(int,input().split()))
b=[1 for x,y,z in zip(a,a[1:],a[2:]) if x+z==2*y]
print("So bo 3 lien tiep csc: ",sum(b))

#lenh while
#nhap n tinh tong cac chu so
n=int(input())
s=0
while n>0:
    s+=n%10
    n//=10
print(s)
#cach 2: print(sum((map(int,input()))))

#giai phuong trinh x^x=a voi a thuoc [1,10^10]
a=float(input())
L,R=1,10
while R-L>1e-5:
    M=(L+R)/2
    if pow(M,M)>a: R=M
    else: L=M
print("x= ",L)

from math import sqrt

#cho hinh tron tam 0, bk r va diem M. tim diem tren duong tron gan M nhat
def kc(x,y,z,t): return ((x-z)*(x-z)+(y-t)*(y-t))
if __name__ == '__main__':
    x0,y0,r,xM,yM=map(float,input().split())
    if kc(x0,y0,xM,yM)<=r*r:
        xP,yP=x0,y0
        while abs(xP-xM)>1e-5 or abs(yP-yM)>1e-5:
            xQ=(xP+xM)/2
            yQ=(yP+yM)/2
            if kc(x0,y0,xQ,yQ)>r*r: xM,yM=xQ,yQ
            else: xP,yP=xQ,yQ
        print(xM,yM)
'''

'''
# 29_08_22
from collections import namedtuple
diem = namedtuple('Point',"x y")
if __name__ == '__main__':
    A=diem(3,4)
    B=diem(5,6)
    print(A)
    print(B.x,B.y)

import math
from collections import namedtuple
diem = namedtuple('Point',"x y")
def kc(A,B): return math.sqrt((A.x-B.x)**2+(A.y-B.y)**2)
def dt(A,B): return A.x*B.y-A.y*B.x
if __name__ == '__main__':
    x,y=map(float,input("A : ").split())
    A=diem(x,y)
    x, y = map(float,input("B : ").split())
    B = diem(x, y)
    x, y = map(float,input("C : ").split())
    C = diem(x, y)
    print("S1= %0.3f"%(abs(dt(A,B)+dt(B,C)+dt(C,A))/2))
    a,b,c=kc(B,C),kc(C,A),kc(A,B)
    p=(a+b+c)/2
    print("S2= %0.3f"%(math.sqrt(p*(p-a)*(p-b)*(p-c))))

#dien tich tu giac
from collections import namedtuple
diem = namedtuple("Diem","x y")
def dt(A,B): return A.x*B.y-A.y*B.x
if __name__ == '__main__':
    D=[]
    for i in range(4):
        x,y=map(float,input("A"+str(i+1)+" : ").split())
        D.append(diem(x,y))
    D.append(D[0])
    s=0
    for A,B in zip(D,D[1:]): s+=dt(A,B)
    print("Dien tich tu giac %.6f"%(abs(s)/2))

#cho tam giac ABC, 1 diem M. tim diem trong(tren) tam giac gan M nhat
from collections import namedtuple
diem = namedtuple("D","x,y")
def dt(A,B): return A.x*B.y-A.y*B.x
def S(A,B,C): return abs(dt(A,B)+dt(B,C)+dt(C,A))/2
def bpkc(A,B): return (A.x-B.x)**2+(A.y-B.y)**2
def tim(A,B,M): #tim diem tren A,B gan M nhat
    while abs(A.x-B.x)>1e-6 or abs(A.y-B.y)>1e-6:
        C=diem((A.x+B.x)/2,(A.y+B.y)/2)
        if bpkc(A,M)>bpkc(B,M): A=C
        else:B=C
    return A,bpkc(A,M)
if __name__ == '__main__':
    x, y = map(float,input().split())
    A = diem(x, y)
    x, y = map(float,input().split())
    B = diem(x, y)
    x, y = map(float,input().split())
    C = diem(x, y)
    x, y = map(float,input().split())
    M = diem(x, y)
    if S(A,B,C)==S(A,B,M)+S(A,C,M)+S(B,C,M): print("%.3f %.3f"%(M.x,M.y))
    else:
        A1,u=tim(B,C,M)
        B1,v=tim(C,A,M)
        C1,t=tim(A,B,M)
        z=min(u,v,t)
        E=A1 if z==u else (B1 if z==v else C1)
        print("%.3f %.3f" % (E.x, E.y))
'''
#cau truc sinh vien gom ho ten, tuoi, diem
#nhap va xuat
#sap xep ds theo diem giam dan
#sap xep ds theo ten tang dan
#in ra sinh vien co diem cao nhat
from collections import namedtuple
sv=namedtuple('SV',"ten tuoi diem")
def nhap(fname):
    f=open(fname,"r")
    S=[]
    for i in range(int(f.readline())):
        a,b,c=f.readline().rsplit(None,2)
        S.append(sv(a,int(b),float(c)))
    f.close()
    return S
def xuat(S):
    for s in S: print("%-20s %5d %6.2f"%(s.ten,s.tuoi,s.diem))
if __name__ == '__main__':
    S=nhap("sv.txt")
    print("Danh sach sinh vien vua nhap")
    xuat(S)
    print("Danh sach diem giam dan")
    S.sort(key=lambda x:x.diem,reverse=True)
    xuat(S)
    print("Danh sach ten tang dan")
    S.sort(key=lambda x:x.ten.split()[-1])
    xuat(S)
    print("Sinh vien co diem cao nhat",max(S,key=lambda x:x.diem))
    print("Tuoi trung binh %f"%(sum([x.tuoi for x in S])/len(S)))
    print("Danh sach sv co diem >6")
    T=[x for x in S if x.diem>6]
    xuat(T)
