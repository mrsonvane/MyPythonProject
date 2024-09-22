#By using + operator
t1=("A","b",20,40,50)
t2=("V",30,11,55,66)
t3=t1+t2
print(t3)

#By using append
list1=list(t1)
list2=list(t2)
list1.append(list2)
print(list1)
t3=tuple(list1)
print(t3)