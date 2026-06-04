num = list(map(int,input().split()))
ls=[]
ls2=[]
for i in num:
    if i  in ls:
        ls2.append(i)
    else:
        ls.append(i)

print(set(ls2))        
