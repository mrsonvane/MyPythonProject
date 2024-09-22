#An escape character is blackslash "\"followed by the character we want to insert
#\"\"- insert double quotes
#\'\'- insert single quotes
#\\- insert one blackslach
# \n insert new line
#\t- Inert tsb space
#\b- to give backspace

data="I am \"Madhu\" and i am from Latur"
data1="I am \'Madhu\' and i am from Latur"
data3="I am \\Madhu and i am from Latur"
data4="I am Madhu \n i am from Latur"
data5="I am Madhu\t and i am from Latur"
data6="I am Madhu \band i am from Latur"
print(data)
print(data1)
#print(data2)
print(data3)
print(data4)
print(data5)
print(data6)

