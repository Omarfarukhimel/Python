a=['omar',25,True,"False"]
print(a[2])            #Second element print

print(a[1:3])          #print 1st and 3rd element print
a.insert(3,20)         #20 insert at the 3rd position
print(a)

a.append('faruk')     #element add at the last position
print(a)

a.pop()               #delete last element
print(a)

a.pop(2)              
print(a)
a.remove('omar')
print(a)
pos=a.index(20)
print('position of the element',+pos)

print('\n')

print('convert list into tuple')
y=["osman",25,False]
print('list:-',y)
x=tuple(y)
print("tuple:-",x)