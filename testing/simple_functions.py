def sum_two_numbers(a, b):
    """
    Should not work with invalid SUM data types.

    :param a: any number type (int, float, Decimal)
    :param b: any number type (int, float, Decimal)
    :return: sum of a & b
    """

    try:
        str_a, str_b = str(a), str(b)
        return int(eval(f"{str_a} + {str_b}"))
    except:
        return
