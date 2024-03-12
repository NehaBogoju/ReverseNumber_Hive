n=int(input())
if n<0:
    sign=-1
    n=-n
else:
    sign=1

m=int(str(n)[::-1])*sign
print(m)
