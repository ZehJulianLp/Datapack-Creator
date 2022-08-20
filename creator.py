from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

print("Welcome to the Datapack Creator!")
print("Please select the folder you want to create the datapack in.")
while True:
    path = askdirectory(title='Select your folder where you want to create the datapack')
    if path == "":
        print("You didn't select a folder, pls try again.")
    else:
        break
print(f"You selected the folder: {path}")
print("Please enter the name of the datapack.")
while True:
    name = input("Name: ")
    if name == "":
        print("You didn't enter a name, pls try again.")
    else:
        break
print("Please Enter the description of the datapack.")
while True:
    description = input("Description: ")
    if description == "":
        print("You didn't enter a description, pls try again.")
    else:
        break

print("Please enter a custom namespace.")
while True:
    namespace = input("Namespace: ")
    if namespace == "":
        print("You didn't enter a namespace, pls try again.")
    else:
        break

print("Starting to create the datapack...")
#create pack.mcmeta with formatted json
os.mkdir(f"{path}/{name}")
with open(f"{path}/{name}/pack.mcmeta", "w") as f:
    f.write(f'{{"pack":{{"pack_format":7,"description":"{description}"}}}}')
print("Created pack.mcmeta")
os.mkdir(f"{path}/{name}/data")
os.mkdir(f"{path}/{name}/data/{namespace}")
os.mkdir(f"{path}/{name}/data/{namespace}/functions")
#create tick function file
with open(f"{path}/{name}/data/{namespace}/functions/tick.mcfunction", "w") as f:
    f.write("#tick function")
print("Created tick function")
#create load function file
with open(f"{path}/{name}/data/{namespace}/functions/load.mcfunction", "w") as f:
    f.write("#load function\n")
    f.write(f"say Loaded {name}!")
print("Created load function")
#create minecraft:load tag
os.mkdir(f"{path}/{name}/data/minecraft")
os.mkdir(f"{path}/{name}/data/minecraft/tags")
os.mkdir(f"{path}/{name}/data/minecraft/tags/functions")
with open(f"{path}/{name}/data/minecraft/tags/functions/load.json", "w") as f:
    f.write(f'{{"values":["{namespace}:load"]}}')
print("Created minecraft:load tag")
#create minecraft:tick tag
with open(f"{path}/{name}/data/minecraft/tags/functions/tick.json", "w") as f:
    f.write(f'{{"values":["{namespace}:tick"]}}')
print("Created minecraft:tick tag")
print("Finished creating the datapack!")
