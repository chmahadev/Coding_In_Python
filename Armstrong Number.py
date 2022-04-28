#this program will print wheather the number is armstrong or not 


def arm(num):
    if (num == '0'):
        return('oops wrong number! please enter number other than 0')
    elif (len(num)<=2):
        return('plese enter 3 digit number')
        
    else:
        sum_ = 0   #creating a sum variable to store the summation of digits after the cube calculation
    
        for i in num:
            #print(i)
            sum_ = sum_ + (int(i)**3)
            #print(sum_)
    #print(sum_)
        if (sum_ == int(inp_num)):
            print('Congratulations! You got the Armstrong number')
        else:
            print('OOps No! its not an Armstrong number')
        return None


inp_num = input('Please enter the number ')

num = [int(x) for x in inp_num.split(",")]
#print(num)

print(arm(inp_num))
