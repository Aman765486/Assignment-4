# Program to read a file and handle errors

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("--- File Content ---")
        # Print each line one by one
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
