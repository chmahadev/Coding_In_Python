#this program will accept the string containing numbers and string and will output only numbers

inp_str = input("please enter the string :")

def onlyNum(inp_str):
    fin_list = []
    for i in inp_str:
        #print(i)
        if(i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9'):
            fin_list.append(i)
        #print(fin_list)
    return print(fin_list)
    
print(onlyNum(inp_str))