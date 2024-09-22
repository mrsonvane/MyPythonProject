fruits=["Apple","Banana","Cherry","Guava"]
print("List before update",fruits)
newlist=[i for i in fruits if i !="Apple"]
print(newlist)

list1=[]
for i in fruits:
    if i !="Apple":
        list1.append(i)
        print(list1)

list2=[]
for i in fruits:
    if "Apple" not in i:
        list2.append(i)
        print(list2)