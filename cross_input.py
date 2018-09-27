import numpy as np

items = []
max = 3

while len(items) < max:
    item = input("Add an element to the list: ")
    items.append(int(item))
    print("The length of the list is now increased to {:d}." .format(len(items)))

print(items)

things = []
values = 3

for i in range(0, values):
    thing = input("Add an element to the second list: ")
    things.append(int(thing))
    print("The length of the second list is now increased to {:d}. " .format(len(things)))

print(things)

z = np.cross(items, things)
print("The cross product of the two lists are: ", z)
