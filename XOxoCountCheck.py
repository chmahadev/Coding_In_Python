#this program will accept a string by user and check if count of x and o's is equal or not

striing = input("please enter the string: ")

def xEqualOCheck(striing):
    countx = 0
    counto = 0
    for i in striing:
        
        if (i == 'X' or i == 'x'):
            countx = countx + 1
            #print(countx)   this line is used for debugging
        elif(i == 'O' or i == 'o'):
            counto = counto + 1
            #print(counto)  and this as well
    if countx == counto:
        return True
    else:
        return False
        
print(xEqualOCheck(striing))