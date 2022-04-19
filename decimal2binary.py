#this program will accept the decimal number from user and print its binary number as output
userinp = input("enter the number you want to convert ")
numb = int(userinp)

def DecToBinary(numb):
    if numb>=1:
        DecToBinary(numb//2)
        print(numb%2, end=" ")
        

DecToBinary(numb)
