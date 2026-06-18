dict = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78,
    "David" : 90,
    "Eve" : 88
}

name = input("Enter the name of the student: ")
if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("student not found.")