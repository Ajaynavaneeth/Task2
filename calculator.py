print("******* CALCULATOR *******")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
#MAIN 
num1=int(input("ENTER NUMBER 1 :"))
num2=int(input("ENTER NUMBER 2 :"))
print("What operation should be performed ")
print("Click 1 for Add")
print("Click 2 for Subtract")
print("Click 3 for Multiply")
print("Click 4 for Divide")
o=int(input())
if(o==1):
    print("Result is ",add(num1,num2))
elif(o==2):
    print("Result is",sub(num1,num2))
elif(o==3):
    print("Result is ",mul(num1,num2))
elif(o==4):
    print("Result is ",div(num1,num2))
else:
    print("INVALID INPUT")

  

        

