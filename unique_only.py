def uniques_only(iterable):
    uniques = []
    for item in iterable:
        if item not in uniques:
            uniques.append(item)
    print(uniques)

uniques_only([1, 1, 2, 2, 3, 4, 4, 3, 6, 7, 7])



