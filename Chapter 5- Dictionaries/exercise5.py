pets = []

pet = {
    'animal':'cat' , 
    'name':'mimi',
    'age':'10',
    'eats':'cat food' ,
}
pets.append(pet)

pet = {
    'animal':'dog' ,
    'name':'viva' , 
    'age':'7' , 
    'eats':'dog food' ,
}
pets.append(pet)

for pet in pets:
    print("\nThings I know about " + pet['name'].title() + ":" )
    for key, value in pet.items():
        print(key + ":" + str(value))