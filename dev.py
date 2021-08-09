def to_str(a):
    tmp = []
    for i in a:
        tmp.append(str(i))
    return " ".join(tmp)


to_str([1, 2, 3])