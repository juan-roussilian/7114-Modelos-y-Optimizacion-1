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

#for prenda in prendas:
    # verifico que no tenga incompatibilidades con las prendas de la listas
    #     si tiene, creo su propia lista
    #     si no, la agrego a una lista
    
# Escribo cada lista de lavado en archivo laundry file
# Salgo ordenadamente

