def divisors(integer):
    div = integer-1
    res = []

    while div != 0:
        if integer % div == 0 and div != 1:
            res.append(div)
            div = div - 1
        else:
            div = div - 1

    if len(res) == 0:
        return print(f"{integer} is prime")
    return res


divisors(29)
