fruits=["Apple","Banana","Cherry","MAngo","Guava","Kiwi"]
newlist=[]
for i in fruits:
    if "a" in i:
        newlist.append(i)
        print(i)                                #Normal way

newlist=[i for i in fruits if "a" in i]         #By using list comprehension
print(newlist)