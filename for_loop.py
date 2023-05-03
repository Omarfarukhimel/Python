print('select an intem')
print('1. ascending order ')
print('2. descending order')
print("""
                    *
                    **
3. Pattern like     ***
                    ****""")
print("""
                    ****
                    ***
4. Pattern like     **
                    *""")
print("5. odd number")
print("6. even number")
print("7. finding the number odd or even")

item=input("select:-")
if item=="1":
    a=int(input("enter a number to start the order :"))
    b=int(input("enter a number to close the order :"))
    for i in range (a,b):
        print(i)

elif item== "2":
    a=int(input("enter a number to start the order :"))
    b=int(input("enter a number to close the order :"))
    for i in reversed(range (a,b)):
        print(i)
elif item == '3':
    n = int(input('Enter the number of lines: '))
    for i in range(1, n+1):
        print('*'*i)

elif item == '4':
    n = int(input('Enter the number of lines: '))
    for i in reversed(range(1, n+1)):
        print('*'*i)

elif item == '5':
    a = int(input('Enter a starting number: '))
    b = int(input('Enter an ending number: '))
    for i in range(a, b+1):
        if i % 2 == 1:
            print(i)

elif item == '6':
    a = int(input('Enter a starting number: '))
    b = int(input('Enter an ending number: '))
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)

elif item == '7':
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        print('The number is even.')
    else:
        print('The number is odd.')

else:
    print("not valid")
          