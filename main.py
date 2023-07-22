PLACEHOLDER = "[name]"

with open("./Inputs/receipient_names.txt") as names_file:
    receipient_names = names_file.readlines()


with open("./Inputs/template.txt") as draft:
    letter = draft.read()
    for name in receipient_names:
        stripped_name = name.strip()
        final_letter = letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Outputs/letter_for_{stripped_name}.txt",mode="w") as write_letter:
            write_letter.write(final_letter)
