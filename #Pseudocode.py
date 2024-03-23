#Pseudocode 

def print_fancy(text, color_code):
    fancy_text = ""
    for char in text:
        fancy_text += char.upper() + " "

    line_length = len(fancy_text) + 4  
    line = "\033[{}m{}\033[0m".format(color_code, "-" * line_length)  
    print(line)
    print("\033[{}m  {}  \033[0m".format(color_code, fancy_text))  
    print(line)


#input name,age,address and dream job


name = input("What is your name?: ")
age = input("What is your age?: ")
address = input ("What is your address?: ")
dream_job = input("What is your dream job?: ")


#print all 

print("Name:", name)
print("Age:" , age)
print("Address:", address)
print("Dream Job:", dream_job)

#print all with fancy text


