def encryption(s):
    n=len(s)
    a=(math.sqrt(n))
    if int(a)==a:
        r=math.floor(a)
        c=math.ceil(a)
    else:
        r=math.floor(a)
        c=math.ceil(a)
    if r*c<n:
        r+=1
    k=0
    arr=[]
    for i in range(r):
        l=[]
        for j in range(c):
            if k<n:
                l.append(s[k])
                k+=1
            else:
                l.append(" ")
        arr.append(l)
    print(arr,r,c)
    k=0
    v=''
    for i in range(c):
        for j in range(r):
            if arr[j][i]==" ":
                continue
            v+=arr[j][i]
            k+=1
        v+=' '
    return v
#rc
