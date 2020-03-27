cases1 = {
    (1, 3, 5, 7, 2, 4, 6, 8): True,
    (1, 3, 5, 2, 7, 4, 6, 8): False,
    (2,): True,
    (1,): True,
    (2, 1): False,
    (1, 2): True
}

cases2 = {
    (1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, None, 9): (8, 4, 2, 0, 2, 1, 0, 0, 0)
    # level order of the node.size
}

"""
key : ((tree nodes stored in a map),(k numbers))
value : results
"""
cases3 = {
    ((((3, 1),),  # Root node , contains 3 children and it's value is 1
      ((2, 2), (1, 3), (0, 4)),
      ((3, 5), (0, 6), (0, 7)),
      ((0, 8), (0, 9), (0, 10))),
     (0, 1, 2, 3, 4)  # some k numbers to test
     ): [6, 1, 1, 2, 0]
}
