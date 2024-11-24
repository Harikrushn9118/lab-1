# pref sum

arr = [2,1,3,4,5,7,8,9,9]
ps = []
Q = [[0,3],[2,8],[3,5],[4,7]]
ps.append(arr[0])
for i in range(1,len(arr)):
    ps.append(arr[i]+ps[i-1])
print(ps)

for i in range(len(Q)):
    x = Q[i][0]
    t = Q[i][1]
    if x==0:
        print(ps[t])
    else:
        print(ps[t]-ps[x-1])


# differencty arr
arr = [13,11,10,2,4,6,7,9,1,0]
# l,r = map(int,input().split())
# x = int(input())
# ds = []
# for i in range(l):
#     ds.append(arr[i])
# for i in range(l,r+1):
#     ds.append(arr[i]+x)
# for i in range(l+1,len(arr)):
#     ds.append(arr[i])
ds = []
ds.append(arr[0])
for i in range(len(arr)):
    el = arr[i]+ds[i-1]
    ds.append(el)
print(ds)



n = int(input())
a = list(map(int,input().split()))
b = len(a)
s = 0
d = 0
a.sort()
if b%2!=0:
    for i in range(b):
        if i%2==1:
            d += a[i]
        else:
            s += a[i]
else:
    if b%2==0:
        for i in range(b):
            if i%2==1:
                s += a[i]
            else:
                d += a[i]
print(s,d)


n = int(input())
a = list(map(int,input().split()))
a.sort()
count = 1
max_count=0
for i in range(n-1,-1,-1):
    if a[i]==a[i-1]:
        count+=1
        if count>max_count:
            max_count=count
if count==0:
    print(1)
else:
    print(max_count)

n = int(input())
a = list(map(int,input().split()))
count = 0
max_count=0
for i in range(1,n):
    if a[i-1]==a[i]:
        count+=1
        if count>max_count:
            max_count=count
print(max_count)

n = int(input())
a = list(map(int, input().split()))
a.sort()
count=1
maxi=1
for i in range(1,n):
    if a[i] == a[i-1]:
        count+=1
    else:
        maxi=max(maxi, count)
        count=1
maxi = max(maxi, count)
print(maxi)

n = int(input())
a = list(map(int, input().split()))
s = 0
d = 0  
l = 0
r = n - 1
t = 0  

while l <= r:
    if a[l] > a[r]:
        chose = a[l]
        l += 1
    else:
        chose = a[r]
        r -= 1

    if t == 0:  
        s += chose
        t = 1
    else:  
        d += chose
        t = 0
print(s, d)


a = input().strip()
b = input().strip()
c = input().strip()
vowel = ['a','e','i','o','u']
counta=0
countb=0
countc=0
for i in range(len(a)):
    if a[i] in vowel:
        counta+=1
for i in range(len(b)):
    if b[i] in vowel:
        countb+=1
for i in range(len(c)):
    if c[i] in vowel:
        countc+=1
if counta==5 and countb==7 and countc==5:
    print("YES")
else:
    print("NO")


n,k = map(int,input().split())
b = []
for _ in range(n):
    p,t = map(int,input().split())
    d = []
    d.append(p)
    d.append(t)
    b.append(d)
b = sorted(b,key=lambda x:(-x[0],x[1]))
sume = 0
for i in range(len(b)):
    if b[i][0]==b[k-1][0] and b[i][1]==b[k-1][1]:
        sume+=1
print(sume)

def binary_(arr,x):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for query in b:
    if binary_(a,query):
        print("YES")
    else:
        print("NO")

S = input().strip()
uc = 0
lc = 0
a = "qwertyuioplkjhgfdsazxcvbnm"
b = "QWERTYUIOPLKJHGFDSAZXCVBNM"
for i in S:
    if i in a:
        lc+=1
    else:
        lc+=1
if lc>=uc:
    n = S.lower()
    print(n)
else:
    n =S.upper
    print(n)


S = input().strip()
uc = 0  
lc = 0  
for i in S:
    if i.islower():
        lc += 1
    elif i.isupper():
        uc += 1
if lc >= uc:
    n = S.lower()
else:
    n = S.upper()
print(n)