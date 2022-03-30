l = []
n = int(input("enter length"))
i = 1
while i < n + 1:
    e = int(input("enter element"))
    l.append(e)
    i = i + 1

print(l)
even = []
for j in l:
    if (j % 2 == 0):
        even.append(j)
even.sort()
print(even[0])