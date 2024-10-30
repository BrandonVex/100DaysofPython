#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

# Define base directory for easier path management
base_dir = "REPLACE WITH DIRECTORY PATH"

# Paths to the input files and output folder
names_path = os.path.join(base_dir, "Input/Names/invited_names.txt")
letter_path = os.path.join(base_dir, "Input/Letters/starting_letter.txt")
output_dir = os.path.join(base_dir, "Output/ReadyToSend")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Check if input files exist
if not os.path.exists(names_path):
    print(f"Error: 'invited_names.txt' not found at {names_path}.")
elif not os.path.exists(letter_path):
    print(f"Error: 'starting_letter.txt' not found at {letter_path}.")
else:
    # Open the file with the names
    with open(names_path) as names_file:
        # Read all names from the file
        names_list = names_file.readlines()
    
    # Open the file with the starting letter template
    with open(letter_path) as letter_file:
        # Read the template content
        letter_content = letter_file.read()
    
    # For each name in the list
    for name in names_list:
        # Strip any leading/trailing whitespace from the name
        stripped_name = name.strip()
        # Replace the placeholder with the actual name
        personalized_letter = letter_content.replace("[name]", stripped_name)
        
        # Create a new letter file in the output directory
        new_letter_path = os.path.join(output_dir, f"letter_for_{stripped_name}.txt")
        with open(new_letter_path, mode="w") as new_letter_file:
            # Write the personalized letter content
            new_letter_file.write(personalized_letter)
    
    print("Letters created successfully in the 'Output/ReadyToSend' folder.")



