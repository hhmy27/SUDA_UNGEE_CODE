"""
key : sequential storage
value: preorder and inorder values
"""
cases1 = {
    (1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, None, 9): [[1, 2, 4, 5, 7, 8, 3, 6, 9],
                                                                      [4, 2, 7, 5, 8, 1, 3, 6, 9]]

}

cases2 = {
    ((1, 2, 3, 4, 5, 6, 7), 4): (1, 3),
    ((1, 2, 4, 5, 6, 7), 4): None
}