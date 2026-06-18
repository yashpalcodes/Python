list = []

for i in range(1, 11):
    list.append(i)

print(f"original list: {list}")

list2 = list[0:5]
print(f"Extracted first 5 elements: {list2}")

print(f"reversed the extracted list: {list2[::-1]}")