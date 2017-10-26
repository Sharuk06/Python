#Python v2.7 code to implement Serialization and Deserialization

import pickle

num =int(raw_input("Enter the number of integer elements to store : "))
list = []
for x in range(0,num):
    a=int(raw_input())
    list.append(a)

list_string=pickle.dumps(list)
data2=pickle.loads(list_string)

for x in data2:
    print x
