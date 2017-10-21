#Python V3 SOURCE CODE TO IMPLEMENT FILE HANDLING

#Opening a file in R+ mode
file = open("f:\\a.txt","r+")
#Reading the contents of the file
content = file.read()
#List Comprehension 
list = [int(x) for x in content.split()]
print list
