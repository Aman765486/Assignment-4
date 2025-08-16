# Program to write, append, and read a file

# Step 1: Write user input to the file
user_text = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_text + "\n")

# Step 2: Append additional data to the same file
extra_text = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(extra_text + "\n")

# Step 3: Read and display final content of the file
print("\n--- Final File Content ---")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
