#this program will take list of user defined numbers and the type of sort they want to perform. and after that the result will be shown accordingly
lisst = input("enter the numbers separated by space ")
print('/n')
userlist = lisst.split()
types = input("specify the type of sort i.e asc/desc/none ")
user_types = str(types)
def sortFunc(userlist, user_types):
    if user_types == 'asc':
        userlist.sort()
        
    elif user_types == 'desc':
        userlist.sort(reverse= True)
        
    else:
        userlist
    
    return userlist
    
print("the sorted list is",sortFunc(userlist, user_types))
