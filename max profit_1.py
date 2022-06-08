def profit(): #function defination
    #list comprehension for taking input from user
    a = [int(i) for i in input("enter array elements of array using spaces").split()] 
    print("The array u have entered is :"a)  #printing the array given by user
    def gcd(a,b):  #gcd function defination using recursion
        if(b==0):
            return abs(a)
        else:
            return gcd(b,a%b)
    profit=0
    while(len(a)!=1):
        i=0
        HCF = gcd(a[i],a[i+1])
        profit += a[i]+a[i+1]
        del a[0:2]
        a.append(HCF)
    print(profit)
    
profit()  #calling the function

