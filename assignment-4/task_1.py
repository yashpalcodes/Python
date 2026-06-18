file_path = "sample.txt"
i = 1
try:    
    with open(file_path, "r") as file:
        content = file.read()
        for line in content.splitlines():
            print(f"Line {i} : {line}")
            i += 1

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
