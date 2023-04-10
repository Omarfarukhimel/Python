print("Select an operator for performed")
print("1. add")
print("2. subtract")
print("3. multiplication")
print("4. division")

operation =input("select:-")

if operation == "1":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 print("total sum="+str(float(num1)+float(num2)))

elif operation == "2":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 print("total  subtract ="+str(float(num1)-float(num2)))

elif operation == "3":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 print("total multiplication="+str(float(num1)*float(num2)))

elif operation == "4":
 num1=input("Enter 1st number:-")
 num2=input("Enter 2nd number:-")
 print("total division="+str(float(num1)/float(num2)))

else:
 print("not valid")
