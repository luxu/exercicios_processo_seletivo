

def rotate_an_array(k: int):
    """
    >>> rotate_an_array(1)
    [7, 1, 2, 3, 4, 5, 6]
    >>> rotate_an_array(3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate_an_array(5)
    [3, 4, 5, 6, 7, 1, 2]

    :params n:
    :return:
    """

    array_list = [1, 2, 3, 4, 5, 6, 7]

    for nro in range(k):
        temp = array_list.pop()
        array_list.insert(0, temp)

    return array_list
