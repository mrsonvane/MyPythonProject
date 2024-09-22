dict1={'Name': 'Ram', 'Last_Name': 'Sonvane', 'Age': 45, 'year': 2024, 'DOB': 1990, 'color': 'red'}
print(dict1)
dict1.pop("DOB")            #by using pop delete particular key data
print(dict1)

dict1.update({"Brand":"Honda"})     #Add the item
print(dict1)

dict1.popitem()             #last inserted item will bw delete
print(dict1)

del dict1["Age"]            #delete particular key item
print(dict1)

#del dict1()                 #throws error
#print(dict1)

dict1.clear()                 # output is empty dictionary{}
print(dict1)