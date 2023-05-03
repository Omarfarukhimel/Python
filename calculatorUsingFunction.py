print("Select an operator for performed")
print("1. add")
print("2. subtract")
print("3. multiplication")
print("4. division")
def add(num1,num2):
     sum=float(num1)+float(num2)
     print("sum:-",sum)

def subtract(num1,num2):
  sub=float(num1)-float(num2) 
  print("subtract:-",sub)


def multiplication(num1,num2):
  multiply=float(num1)*float(num2)
  print("total multiplication :-",multiply) 

def division(num1,num2):
  if num1<num2:
    div=float(num1)/float(num2)
    print("division:-",div)

  else:
    print("number 2 is grater then number1") 

operation =input("select:-")

if operation == "1":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 add(num1,num2)
 

elif operation == "2":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 subtract(num1,num2)

elif operation == "3":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 multiplication(num1,num2)

elif operation == "4":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 division(num1,num2)
else:
 print("not valid")