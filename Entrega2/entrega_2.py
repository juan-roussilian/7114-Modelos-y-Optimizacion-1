def is_incompatible(a_cloth, another_cloth):
    incompatible = False
    if (a_cloth in incompatibilities[another_cloth]):
        incompatible = True
    if (another_cloth in incompatibilities[a_cloth]):
        incompatible = True
    return incompatible

def write_washing_in_file(file, washing_elements, washing_n):
    for cloth in washing_elements:
        file.write(f"{cloth} {washing_n}\n")

clothes_file = open("./segundo_problema.txt")
laundry_file = open("./resultado.txt","w")
incompatibilities = {}
clothes = []

# Read all lines from file and add them to either incompatibilities dict or clothes list.
for line in clothes_file:
    chars = line.split()
    if chars[0] == "e":
        #If the cloth No. already has a list of incopatible clothes, append the new one to it.
        if chars[1] in incompatibilities:
            incompatibilities[chars[1]].append(chars[2])
        #If it does not have any incoptaibility created yet, add a list with the current cloth to the dictonary on its key.
        else:
            incompatibilities[chars[1]] = [chars[2]]

    elif chars[0] == "n":
        clothes.append([chars[1], chars[2]])

washes = []
#print(clothes)
for cloth in clothes:
    incompatible_with_all = True
    for wash in washes:
        incompatible_with_wash = False
        counter = 0
        # Check against all clothes in current wash if is incompatible
        while(not incompatible_with_wash and counter < len(wash)):
            incompatible_with_wash =  is_incompatible(cloth[0], wash[counter])
            counter += 1
        
        if(not incompatible_with_wash):
            wash.append(cloth[0])
            incompatible_with_all = False
            break

    # If no compatible washes are found,create a new one with the incompatible cloth
    if(incompatible_with_all):
        washes.append([cloth[0]])
wash_counter = 1

for washing in washes:
    write_washing_in_file(laundry_file, washing, wash_counter)
    wash_counter += 1