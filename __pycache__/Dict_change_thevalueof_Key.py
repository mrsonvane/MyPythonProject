dict1={
    "Name":"Madhu",
    "Last_Name":"Dahiphle",
    "Age":32
}
dict1["Age"]=45
dict1["Name"]="Ram"
print(dict1)

#update using update() method
dict1.update({"year":2024})
dict1.update({"Last_Name":"Sonvane"})
dict1.update({"DOB":1990})
dict1["color"]="red"
print(dict1)