import main, test


def createPizza(file):
    paired = main.parseInput(file)
    group = paired.copy()
    while len(group)>1:
        group = merge(group)
    print("Score:", end=" ")
    print(test.test(group[0]["liked"], paired))
    return group[0]["liked"]

def merge(group):
    pref1 = group[0]
    pref2 = group[1]
    for i in pref1["liked"]:
        if i in pref2["disliked"]:
            group.pop(1)
            return group
    for j in pref1["disliked"]:
        if j in pref2["liked"]:
            group.pop(1)
            return group

    group[0] = {
        "liked": list(set(pref1["liked"] + pref2["liked"])),
        "disliked": list(set(pref1["disliked"] + pref2["disliked"]))
    }

    group.pop(1)
    return group


createPizza(open("input/e.txt"))