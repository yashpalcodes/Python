content = input("Enter the content to write to the file: ")

try:
    with open("output.txt", "w") as file:
        file.write(content)
        print("Content written to 'output.txt' successfully.")
except Exception:
    print(f"error : {Exception}")


additional_content = input("Enter additional content to append to the file: ")

try:
    with open("output.txt", "a") as file:
        file.write("\n" + additional_content)
        print("Additional content appended to 'output.txt' successfully.")
except Exception:
    print(f"error : {Exception}")   

print("Final content of 'output.txt' : ")

try:
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)
except Exception:
    print(f"error : {Exception}")  