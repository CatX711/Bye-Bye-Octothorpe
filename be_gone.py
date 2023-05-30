import fileinput
import sys
import os

# Define the file path
file_path = "your_file.py"

# Create a temporary file for writing the modified code
temp_file_path = file_path + ".temp"

# Perform the search and replace operation
with fileinput.FileInput(file_path, inplace=True, backup=".bak") as file:
    for line in file:
        # Replace '#' with '//'
        modified_line = line.replace("#", "//")
        print(modified_line, end="")

# Remove the backup file
os.remove(file_path + ".bak")

# Rename the temporary file to the original file name
os.rename(temp_file_path, file_path)

# Print a message indicating the operation is completed
print("Comments have been changed from '#' to '//' successfully.")



// Make sure to replace "your_file.py" with the actual path to your Python file. This code reads the original file line by line, replaces any occurrence of # with //, and writes the modified lines to a temporary file. Then it removes the original file, renames the temporary file to the original file name, and prints a message indicating the completion of the operation.

// Note: It's always a good practice to make a backup of your file before making changes like this, just in case anything goes wrong. The code above creates a backup file with a .bak extension.
