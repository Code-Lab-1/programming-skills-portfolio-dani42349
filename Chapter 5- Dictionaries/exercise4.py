rivers = {
    'nile': 'egypt',
    'jhelum':'Pakistan',
    'congo': 'Africa',
    'Amazon river':'South America',
    'Yellow river':'China',


}

for river, country in rivers.item():
    print("The " + river.title() + "flows through" + country.title() + ".")

print("\nThe rivers are included in this data set:")
for river in rivers.key():
    print("-" + river.title())  

print("\nThe countries are included in this data set:") 
for country in rivers.values():
    print("-"  + country.title())     