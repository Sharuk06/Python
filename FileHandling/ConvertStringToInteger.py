#SOURCE CODE TO IMPLEMENT FILE HANDLING

file = open("f:\\a.txt","r+")
content = file.read()
list = [int(x) for x in content.split()]
print list
