
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


