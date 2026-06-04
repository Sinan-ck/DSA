n = input("Enter the number: ")
d = input("enter the digit: ")
arr=[]
for i in  range(len(n)):
    if n[i]==d:
        t=n[0:i]+n[i+1: len(n)]
    arr.append(int(t))
print(max(arr))
