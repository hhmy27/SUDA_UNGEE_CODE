cases1 = {
    2100: [7, 5, 5, 3, 2, 2]
}

cases2 = {
    (1,): True,
    (1, 2, 3): True,
    (1, 2, 3, 4): False,
    (1, 2, 3, None, 4): False,
    (1, 2, 3, None, 4, None, 5): False,
    (1, 2, 3, 4, 5, 6, 7): True
}
