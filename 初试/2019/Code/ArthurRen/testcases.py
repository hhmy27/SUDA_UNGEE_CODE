# You can add your test cases to the testCases dictionary.

# <editor-fold desc="cases of solution1">

"""
key: tuple of btree under sequential storage
value : list of path (your right answer)
example :
        1
       / \
      2   3
     / \   \
    4  5    6
      / \    \
     7   8    9
"""
cases1 = {
    (1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, None, 9): [1, 3, 6, 9]
}

# </editor-fold>


# <editor-fold desc="cases of solution2">

arcMatrix1 = (
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 1),
    (0, 1, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 1, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 1),
)
vertices1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
i1 = 0
j1 = 3
simplePaths1 = {(0, 1, 3), (0, 2, 3), (0, 9, 1, 3)}

"""
key: tuple (arcMatrix, vertices, i, j)
value : simple paths set(your right answer)
"""
cases2 = {
    (arcMatrix1, vertices1, i1, j1): simplePaths1
}

# </editor-fold>
