
def reverse_words_in_a_string(s: str):
    """
    >>> reverse_words_in_a_string("the sky is blue")
    'blue is sky the'
    >>> reverse_words_in_a_string("comemos uma porção de batata")
    'batata de porção uma comemos'

    :param s :
    :return:
    """

    # 1ª Solução
    # s = list(reversed(s.split()))

    # 2ª Solução
    nv = []
    word = ''
    for c in s:
        if ' ' in c:
            nv.append(word)
            word = ''
        else:
            word += c
    nv.append(word)
    palavra = nv[-1]
    for indice in range(2, len(nv) + 1):
        palavra += ''.join((' ', nv[int(f'-{indice}')]))
    return palavra
