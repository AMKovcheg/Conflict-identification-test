def sum(l_int: list[int]) -> int:
    res = 0

    for i in l_int:
        res += i

    return res

def concat(l_str: list[str]) -> str:
    res = ""

    for s in l_str:
        res += s

    return res