def to_jaden_case(string):
    msg = string.split(" ")
    res = ""
    final = ""
    size = len(msg) - 1

    for x,word in enumerate(msg):
        res = word[0].upper() + word[1:]
        if x == size:
            final = final + res
        else:
            final = final + res + " "
    print(final)


to_jaden_case("How can mirrors be real if our eyes aren't real")