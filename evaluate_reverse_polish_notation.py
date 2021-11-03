

def evaluate_reverse_polish_notation(nrs: list):
    """
    >>> evaluate_reverse_polish_notation(["2", "1", "+"])
    3
    >>> evaluate_reverse_polish_notation(["2", "1", "+", "3", "*"])
    9
    >>> evaluate_reverse_polish_notation(["4", "13", "5", "/", "+"])
    6
    >>> evaluate_reverse_polish_notation(["6", "13", "5", "+", "/"])
    3

    :return:
    """

    # ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    # ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
    # ["6", "13", "5", "+", "/"] -> (6 / (13 + 5)) -> 6

    summ = 0
    numbers = []
    for op in nrs:
        if op.isalnum():
            numbers.append(int(op))
        else:
            numbers.append(op)
            for n in numbers:
                operator = numbers.pop()
                num1 = numbers.pop()
                try:
                    num2 = numbers.pop()
                except:
                    num2 = 0
                if '+' in operator:
                    summ += num1 + num2
                    break
                elif '*' in operator:
                    if num2 == 0:
                        num2 = 1
                    summ *= num2 * num1
                    break
                elif '/' in operator:
                    if num2 == 0:
                        num2 = 1
                    if nrs[-1] == '/':
                        summ /= int(num1 / num2)
                        summ = int(summ)
                    else:
                        summ += int(num2 / num1)
                    break
    return summ
