# when python opens a file, it creates a file object that is used to interact with the file - using computer resources

# with open("my_file.txt") as file: # this is a context manager, it automatically closes the file after the block of code is executed
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# this write mode will overwrite the file - mode = "w"
# with "\n" we can add a new line at the end of the file instead of overwriting it
with open("my_file.txt", mode="w") as file:
    file.write("\nNew text.")
    
# you can also create a file if it doesn't exist, must be in write mode
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
    
# to open a file in another folder you can use the path
# Files/new_file.txt will create a new file in the Files folder
with open("Files/new_file.txt", mode="w") as file:
    file.write("New text.")
    
    

