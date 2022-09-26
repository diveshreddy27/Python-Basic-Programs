def test(s):
    if(len(s)==1):
        return [s]
    a=test(s[1:])
    c=s[0]
    ans=[]
    for comb in a:
        for i in range(len(comb)+1):
            x=comb[:i]+c+comb[i:]
            ans.append(x)
    return ans

s=input()
fans=test(s)
print(fans)
