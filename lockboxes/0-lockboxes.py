#!/usr/bin/python3
"""
    canUnlockAll: having n number of 'blocked boxes' (a list of lists) with
    keys inside each, it determines if all the boxes can be open taking into
    account that the first one is always open and it can contain keys for the
    rest of them
"""

def canUnlockAll(boxes):
    """
        
    """
    if len(boxes) == 1:
        return True
    if len(boxes[0]) == 0:
        return False
    array = boxes[0]
    for i in range(len(array) - 1):
        if array[i] > len(boxes) - 1:
            array.pop(i)
    array2 = []
    while not len(array) > len(boxes) - 1 and array2 != array:
        array2 = array.copy()
        for i in range(len(array2)):
            array += boxes[array2[i]]
            array = list(set(array))
    for i in range(len(array) - 1):
        if array[i] == 0:
            array.pop(i)
    if len(array) == len(boxes) -1:
        return True
    return False
