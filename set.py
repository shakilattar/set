def func():
    s1 = {2, 4, 6, 8, 10, 12}
    print(s1)
    s1.add(14)
    print(s1)

    s2 = frozenset([1, 3, 5, 7, 9, 11, 13])
    print(s2)
    # add is not possible in frozenset because frozenset is immutable


func()
