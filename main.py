#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as invited:  # Open folder with names
    names = invited.read()
names = names.split("\n")  # Split all names

for name in names:
    with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as letter:  # Read letter
        letter_to = letter.read().replace("[name]", name)  # Replace [name] with invited name
        address = f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt"  # Make the address
        with open(address, mode="w") as new_letter:  # create new folder and put the letter_to
            new_letter.write(letter_to)
