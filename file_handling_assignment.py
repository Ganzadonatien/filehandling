# file_handling_assignment.py

# File Creation and Writing
def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is a number: 12345\n")
            file.write("This is the third line.\n")
        print("File created and written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while writing the file: {e}")
    finally:
        print("File write operation complete.")

# File Reading and Displaying
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Reading file content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File read operation complete.")

# File Appending
def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is the fourth line.\n")
            file.write("Here is another number: 67890\n")
            file.write("This is the sixth line.\n")
        print("File appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File append operation complete.")

# Main execution
if __name__ == "__main__":
    create_and_write_file() 
    read_file()              
    append_to_file()       
    read_file()             
