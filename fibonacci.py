# code for fibonacci sequence of n numbers
n = int(input("Enter the number of elements: "))
n1 = 0
n2 = 1

print(n1, end = ", ")
print(n2, end = "")

i = 2
for i in range(2, n):
  n3 = n1 + n2
  print(", ", n3, end = "")
  n1 = n2
  n2 = n3 
  
