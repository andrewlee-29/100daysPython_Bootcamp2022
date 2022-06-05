# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as file:
    names = []
    names = file.read().split()
with open("Input/Letters/starting_letter.txt") as file:
    letter_sample = file.read()

for name in names:
    with open(f"Output/ReadyToSend/{name}.txt",mode="w") as file:
        letter = letter_sample.replace(PLACEHOLDER,name)
        file.write(letter)