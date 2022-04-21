#this is simple program you can use to calculate discounted price

price = int(input("enter the price: "))
disc = int(input("enter % of discount: "))

def discount(price, disc):
    final_price = price - price*(disc/100)
    
    return final_price
    
print("final price after discounts will be :",discount(price, disc))