## Assigning elements to different lists
myList1 = ["C"]
myList2 = []

# Adding Python and JavaScript to myList1
myList1.append("C++")
myList1.append("Java")
myList1.append("Python")
myList1.append("JavaScript")

# Adding 17, 19, 23 to myList2
myList2.append(2)
myList2.append(3)
myList2.append(5)
myList2.append(7)
myList2.append(11)

# The final lists after assigning new elements
print("New myList1 after adding elements is: ",myList1)
print("myList2 after assigning elements to it is: ",myList2)
print() # to give a line gap betweeen lists and tuples


## Accessing elements of a tuple
myTuple1 = ("Maths", "Physics", "Chemistry")
myTuple2 = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

# Accessing element at index 2 in myTuple1
print("Element at index 2 in myTuple1 is: ", myTuple1[2])

# Accessing elements from index 2 to 8 in myTuple2
print("ELements from index 2 to 8 in myTuple are: ", myTuple2[2:9])
print() # to give a line gap between tuples and dictionary


## Deleting different dictionary elements
myDict1_squares = {
    1 : 1,
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25
    }
myDict2 = {
    "C" : "Easy",
    "C++" : "Moderate",
    "Java" : "Tough"
    }
myDict3 = {
    "Name" : "Arjun",
    "Age" : "26"
    }
# Using del to delete elements from the dictionary
del myDict1_squares[2]
del myDict1_squares[5]

# Using pop() to delete element from the dictionary
myDict2.pop("C++")

# Using clear() to delete elementst but not the dictionary
myDict3.clear()

print("myDict1_squares after deletion is: ",myDict1_squares)
print("myDict2 after deletion is: ",myDict2)
print("myDict3 after clear() is: ",myDict3)

    
