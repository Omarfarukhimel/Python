s = input("Enter a string :-")
string = s[::-1]
'''The slicing syntax is string[start:stop:step], 
where start is the starting index, stop is the stopping index(exclusive), 
and step is the step size.'''

if (string==s):
    print("it is  palindrom")
else:
    print("it is not palindrom ")    