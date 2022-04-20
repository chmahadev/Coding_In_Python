#this program will ask the user to enter the desired string and then will display thw vowel count as output on screen
new2 = input("Please enter the word ")

def vowCount(new2):
    count = 0
    for j in new2:
        
        if(j=='a'or j=='e' or j=='i' or j=='o'or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
            count = count +1
    return count       

print(vowCount(new2))
