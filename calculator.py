num1=int(input("enter first number:"))
char=input("enter operation:")
num2=int(input("enter second number:"))
if char=='+':
    print(f"{num1}+{num2} is :",num1+num2)
elif char=='-':
    print(f"{num1}-{num2} is :",num1-num2)
elif char=='*':
    print(f"{num1}*{num2} is :",num1*num2)
elif char=='/':
    print(f"{num1}/{num2} is :",num1/num2)
elif char=='%':
    print(f"{num1}%{num2} is :",num1%num2)
elif char=='**':
    print(f"{num1}**{num2} is :",num1**num2)
else:
    print("enter valid sign (+,-,*,/,%,**)")