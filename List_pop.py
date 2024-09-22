#POP() is used to remove specified index value from the list
list1=["A","B",10,20,30,40,50]
print("List before deletion",list1)
list1.pop(2)
print("List after pop",list1)
#list1.pop(3,6)                                 TypeError: pop expected at most 1 argument, got 2
#print("List after second deletion",list1)