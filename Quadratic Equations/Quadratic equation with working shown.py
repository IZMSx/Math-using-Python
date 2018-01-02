from fractions import gcd

def factors(a,c):
    factors=[]
    num1=0    #Storing the two numbers that mutiply
    num2=0    #to give b
    multiply=abs(a*c)
    for i in range(1,multiply+1):
        if multiply % i==0:
            factors.append(i)
            
    index=0
    success=False
    while not success :
        sto=factors[index]
        factors.pop(index)
        for i in factors:
            for j in factors:
                if b==i+j or b==i-j:
                    num1=i
                    num2=j
            
            if num1+num2 != b:
                num1=-num1
                if num1+num2 != b:
                    num2=-num2
                    if num1+num2 != b:
                        num1=-num1
        if num1+num2==b and num1*num2==a*c:
            success = True
            
        factors.append(sto)
    num=[num1,num2]
    return(num)

def factorization(a,middle1,middle2,c):
    common1=gcd(a,middle1) #common facto in first half 
    common2=gcd(middle2,c) #common factor in second half
    print("%sx(%sx+%s)" % (common1,a//common1,middle1//common1), end=" ")
    print("+ %s(%sx+%s) = 0" % (common2,middle2//common2,c//common2))
    print("(%sx+%s)(%sx+%s) = 0" %(common1, common2 ,a//common1 ,middle1//common1))
    temp1=a//common1
    temp2=middle1//common1
    print("x =",-1*common2/common1,"or x =",-1*temp2/temp1)
    
def working():
    global a,b,c
    print("Enter ax^2 + bx + c = 0")
    a=int(input("ax^2: "))
    b=int(input("bx: "))
    c=int(input("c: "))
    print("\nSolving the equation:")
    if c == 0:
        print("%sx^2 + %sx = 0" % (a,b))
        print("\nWorked Solution:")
        print("x(%sx + %s) = 0" % (a,b))
        print("x=0 or x=",-b/a)
    else: 
        print("%sx^2 + %sx + %s = 0" % (a,b,c))
        num=factors(a,c)
        print("\nWorked Solution:")
        print("%sx^2 + %sx + %s = 0" % (a,b,c))
        print("%sx^2 + %sx + %sx + %s = 0" % (a,num[0],num[1],c))
        factorization(a,num[0],num[1],c)
working()
