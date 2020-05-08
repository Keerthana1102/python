myList = [int(x) for x in input("Enter the list elements separated by ',': ").split(',')]

output = []

for num in myList:
    if num>0:
        output.append(num)
print(output)
