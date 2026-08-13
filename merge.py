def merge(l,r):
    merged=[]
    i,j=0,0
    n,m=len(l),len(r)
    while i<n and j<m:
        if l[i]<=r[j]:
            merged.append(l[i])
            i+=1
        else:
            merged.append(r[j])
            j+=1
    if i<n:
            while i<n:
             merged.append(l[i])
             i+=1    
    elif j<m:
            merged.append(r[j])
            j+=1
    return merged
