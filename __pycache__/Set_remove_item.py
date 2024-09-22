s1={"A","b",True, 1, 4,6,7,8,}
print("Set before remove",s1)
s1.remove("A")
print("Set after remove",s1)

#Remove by using discard method
s1.discard("b")
print("Set after discard",s1)

#s1.remove(10)
#print("Data not exist remove",s1)       #throws error

s1.discard(10)
print("No data to discard",s1)      #No error it display the set

