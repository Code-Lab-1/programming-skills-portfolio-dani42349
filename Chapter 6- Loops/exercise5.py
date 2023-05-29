sandwich_orders = ['Beef' , 'Chicken' , 'Veggi' , 'cheesy' , 'Pastrami']
finished_sandwiches = []

print("Sorry we are all out of Pastrami today.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(" working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
    

