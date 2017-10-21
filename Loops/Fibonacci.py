#SOURCE CODE TO IMPLEMENT FIBONACCI SERIES Python V3
#Declaring list to store fibonacci series
list = [0,1]
#Using for loop to iterate
for i in xrange(2,10):
    a = list[i-1] + list[i-2]
    list.append(a)

#Printing the result
print list

