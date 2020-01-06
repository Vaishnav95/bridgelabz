"""Create a JSON file having Inventory Details for Rice, Pulses and Wheat
with properties name, weight, price per kg.
"""
import json

file = open("inventory.json", 'r')
data = json.load(file)
file.close()

for key in data:
    for value in data[key]:
        price = 0
        weight = 0
        price += int(value['price'])
        weight += int(value['weight'])
        print('Name:', value['name'])
        print('Price:', value['price'])
        print('Weight:', value['weight'])
        print()