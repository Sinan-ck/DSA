def calculator(x,y):
    
    op= input('enter the oparator :\n')
    if op=='+':
        print(x+y)
    elif op=='-':
        print(x-y)
    elif op=='*':
        print(x*y)
    elif op=='/':
        print(f"{x/y}" if  y!=0 else "cant perform oparation")
    else:
        print("invalied oparator")   

a,b= map(int,input("enter two numbers :\n").split())
calculator(a,b)
