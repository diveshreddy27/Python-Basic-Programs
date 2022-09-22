n=input()
a=list(map(int,n))
sum=0
for i in range(len(a)):
    a[i]=a[i]**3
    sum=sum+a[i]
if(n==str(sum)):
    print("armstrong")
else:
    print("not armstrong")