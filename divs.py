a=0
b=1
for i in range(1,100):
    if i%7==0:
        a=a+i
        b=b*i
print("sum",a)
print("multi",b)