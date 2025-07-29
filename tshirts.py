INVALID_INPUT = 'Invalid input'


def size(cms):
    if not isinstance(cms, (int, float)) or cms < 0:
        return INVALID_INPUT
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(38)== 'M')
assert(size(0) == 'S')
assert(size(38) == 'M')
assert(size(42) == 'L')
assert(size(-1) == INVALID_INPUT)
assert(size('abc') == INVALID_INPUT)
assert(size(None) == INVALID_INPUT)
print("All is well (maybe!)")
