#get a list of name and make them title caps and print the list
choice = "y"
name = " "
count = 0
namelist =[]
while choice=='y':
    name = raw_input("Enter a name :")
    namelist.append(name)
    choice = raw_input("try again : y/n")
    count+=1

print namelist
