t1=("A",10,30,50,40,39,50)
list1=list(t1)
list1.remove("A")       #By using remove method
t1=tuple(list1)
print(t1)

#By using pop method
list2=list(t1)
list2.pop(4)
t1=tuple(list2)
print(t1)

#by using del keyword
