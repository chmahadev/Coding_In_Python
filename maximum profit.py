#Maximum Profit problem
#You are given an array A[] of N distinct integers. You can choose two ajecent elemnents, A[i], A[i+1] and replace them with one element 
#with value equal to the Greatest common divisor of A[i] and A[i+1], profit added in that case will be equal to A[i] + A[i+1]. you can do this  
#operation until the size of the array becomes 1
#return the maximum profit we can get
#Example: Input: N=3, A[1,2,3]
#output:7
#


#input array given
a = [1,2,3,4,-5]
profit=0  #initialise the profit to 0
# logic of gcd
def gcd(a,b): 
    if(b==0):
        return abs(a)
    else:
        return gcd(b,a%b)

while(len(a)!=1):  
    i=0
    HCF = gcd(a[i],a[i+1]) #calling gcd
    profit += a[i]+a[i+1] #adding elements values in profit;
    del a[0:2] #deleting  first 2 elements after calculating gcd
    a.append(HCF)  #append the gcd value in last place of list
    
print(profit)


