#this program will ask the user to enter 16 digit credit card number and will 
#return a masked number with only last 4 digits visible
card_num = input("enter the credit card number: ")
import re
def mask(card_num, digits_to_keep=4, mask_char='x'):

    num_of_digits = sum(map(str.isdigit, card_num))
    digits_to_mask = num_of_digits - digits_to_keep
    masked_string = re.sub('\d', mask_char, card_num, digits_to_mask)
    return masked_string

print("card number after masking is: "mask(card_num))

    
    
