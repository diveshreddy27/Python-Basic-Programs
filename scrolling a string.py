import time
s=input()
s=list(s+"                        ")
n=len(s)
while(1):
    c=s[0]
    for i in range(n):
        if(i+1<n):
            s[i]=s[i+1]
    s[i]=c
    print("".join(s))
    time.sleep(1)
