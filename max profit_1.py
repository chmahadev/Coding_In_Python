#Maximum Profit problem
#You are given an array A[] of N distinct integers. You can choose two ajecent elemnents, A[i], A[i+1] and replace them with one element 
#with value equal to the Greatest common divisor of A[i] and A[i+1], profit added in that case will be equal to A[i] + A[i+1]. you can do this  
#operation until the size of the array becomes 1
#return the maximum profit we can get
#Example: Input: N=3, A[1,2,3]
#output:7

# in this solution i have used list comprehension
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

