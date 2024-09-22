dict1={
    "Name":"Madhu",
    "Last_Name":"Dahiphle",
    "Age":32
}
print(dict1)                #origina dictonary
x=dict1.keys()              #original key values
print(x)
y=dict1.values()            #original values
print(y)
dict1["color"]="white"      #Added new key and value data 
print(x)
print(y)
print(dict1)                #dictionary after added data
z=dict1.items()
print(z)

#Add both key and value at time