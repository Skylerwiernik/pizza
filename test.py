def test(answer, paired):
    count = 0

    for person in paired:
        potential = True
        for disliked in person["disliked"]:
            if disliked in answer:
                potential = False
        for liked in person["liked"]:
            if liked not in answer:
                potential = False
        if potential:
            count += 1
    return count
