num=[]
n=int (input("enter range"))
for i in range(1,n+1):
    e=int(input("enter element"))
    num.append(e)
for i in num:
    if i>500:
        break
    elif i>150:
        continue
    elif i % 5 ==0:
        print(i)