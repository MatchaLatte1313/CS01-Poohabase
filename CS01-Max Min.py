Num = int(input('Enter loop count'))
NumTotal =[]
for i in range(Num):
    data = int(input('Enter your Number:'))
    NumTotal += [data]
print(min(NumTotal))
print(max(NumTotal))
