dict1={'Name': 'Ram', 'Last_Name': 'Sonvane', 'Age': 45, 'year': 2024, 'DOB': 1990, 'color': 'red'}
for i in dict1:
    print(i)            #print all key names
for x in dict1:
    print(dict1[x])     #print all values
    
for z in dict1:
    print(z,dict1[z])   #print all keys and values

for a in dict1.keys():  #print keys
    print(a)

for b in dict1.values():    #print values
    print(b)

for c,d in dict1.items():   #print both keys and values
    print(c,d)