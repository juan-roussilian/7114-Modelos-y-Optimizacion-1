def is_incompatible(a_cloth, another_cloth):
    if (a_cloth in incompatibilities[another_cloth]) or (another_cloth in incompatibilities[a_cloth]):
        return True
    else:
        return False

clothes_file = open("primer_problema.txt")
laundry_file = open("resultado.txt","w")
incompatibilities = {}
clothes = []

# Read all lines from file and add them to either incompatibilities dict or clothes list.
for line in clothes_file:
    chars = line.split()
    if chars[0] == "e":
        if chars[1] in incompatibilities:
            incompatibilities[chars[1]].append(chars[2])
        else:
            incompatibilities[chars[1]] = [chars[2]]

    elif chars[0] == "n":
        clothes.append([chars[1], chars[2]])

washes = []
for cloth in clothes:
    incompatible_with_all = True
    for wash in washes:
        incompatible_with_wash = True
        # Check against all clothes in current wash if is incompatible
        for washed_cloth in wash:
            incompatible_with_wash =  is_incompatible(cloth[0], washed_cloth)

        if(not incompatible_with_wash):
            wash.append(cloth[0])
            incompatible_with_all = False
            break
    # If no compatible washes are found,create a new one with the incompatible cloth
    if(incompatible_with_all):
        washes.append([cloth[0]])



    # Salgo ordenadamente

