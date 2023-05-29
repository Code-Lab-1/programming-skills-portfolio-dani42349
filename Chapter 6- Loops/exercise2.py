prompt = "/nWhat is your age?"
prompt +="/nEnter 'quit' when finished"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Will get free ticket")
    elif age < 12 :
        print("your ticket is 12$")
    else :
        print("your ticket is 15$")
