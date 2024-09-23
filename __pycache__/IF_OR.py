a=20
b=3
c=40
if a>b or c>a:      # one condition is true
    print("C is grater")        
if a>b or b>c:          # No output because no condition is true
    print("B grater")   

if a>b or c>b:
    print("Both conditions true")