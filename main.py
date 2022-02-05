# Gets all ingredients with positive scores
def getLiked(file):
    paired = parseInput(file)
    ingredients = {}
    for person in paired:
        for ingredient in person["liked"]:
            if ingredient in ingredients.keys():
                ingredients[ingredient] += 1
            else:
                ingredients[ingredient] = 1
        for ingredient in person["disliked"]:
            if ingredient in ingredients.keys():
                ingredients[ingredient] -= 1
            else:
                ingredients[ingredient] = -1

    liked_ingredients = {}
    for ingredient in ingredients.keys():
        if ingredients[ingredient] >= 1:
            liked_ingredients[ingredient] = ingredients[ingredient]
    return liked_ingredients


def parseInput(file):
    file = [line for line in file]
    # Delete first line if not already removed
    if " " not in file[0]:
        file.pop()
    paired = []
    p = {}

    for line in file:
        s = line.strip()[2:]
        if p == {}:
            p["liked"] = s.split()
        else:
            p["disliked"] = s.split()
            paired.append(p)
            p = {}
    return paired
