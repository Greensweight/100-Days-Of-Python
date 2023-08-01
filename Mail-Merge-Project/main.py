#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# My implementation #
# letter = open("./Input/Letters/starting_letter.txt", "r")
# template_ltr = letter.read()
# names = open("./Input/Names/invited_names.txt", "r")
# trimmed_names = []

# for name in names:
#     new_name = name.strip()
#     trimmed_names.append(new_name)

# for name in trimmed_names:
#     with open(f"./Output/ReadyToSend/new_letter_{name}.txt", mode="w") as file:
#         edited_text = template_ltr.replace("[name]", f"{name}")
#         file.write(edited_text)


# Course implementation

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
