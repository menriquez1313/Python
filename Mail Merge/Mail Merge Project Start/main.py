#Create letters with a given list of names and a default letter syntax. 
   
PLACEHOLDER ="[name]"

with open("./Mail Merge Project Start/input/names/invited_names.txt", mode="r") as names:     
    read_names = names.readlines()
    print(read_names)
    
with open("./Mail Merge Project Start/input/Letters/starting_letter.txt",mode="r") as letter_file:
    letter_contents = letter_file.read()
    for name in read_names:
        stripped_name = name.strip() #strips away the spaces
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Mail Merge Project Start/output/ReadyToSend/letter_for_{stripped_name}",mode="w") as completed_letter:
            completed_letter.write(new_letter)

   