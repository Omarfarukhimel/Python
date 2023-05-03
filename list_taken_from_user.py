
# list=[]
# size=int(input("Enter the array size:-"))

# for element in range(0,size):
#     list.append(int(input("Enter element:-")))

# print(list)
# print("data type",type(element))
   
     

my_list=[]
N = int(input("enter element size"))
for i in range(N):
        lst=input("enter element:-").split()
        if lst[0]=="insert":
            my_list.insert(int(lst[1]),int(lst[2]))
        elif lst[0]=="print":
            print(my_list)
        elif lst[0]=="remove":
            my_list.remove(int(lst[1]))
        elif lst[0]=="append":
            my_list.append(int(lst[1]))
        elif lst[0]=="sort":  
            my_list.sort()
        elif  lst[0]=="pop": 
            my_list.pop()
        else:
            my_list.reverse()
