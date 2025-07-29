INVALID_INPUT = 'Invalid input'


# Refactored function for clarity
def size(cms):
    if not isinstance(cms, (int, float)) or cms < 0:
        return INVALID_INPUT
    if cms < 38:
        return 'S'
    if 38 <= cms < 42:
        return 'M'
    if cms >= 42:
        return 'L'
    return INVALID_INPUT


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(38) == 'M')
assert(size(0) == 'S')
assert(size(38) == 'M')
assert(size(42) == 'L')
assert(size(-1) == INVALID_INPUT)
assert(size('abc') == INVALID_INPUT)
assert(size(None) == INVALID_INPUT)
assert(size(41.9) == 'M')
assert(size(42.0) == 'L')
assert(size(100) == 'L')
assert(size(37.999) == 'S')
assert(size(38.000) == 'M')
assert(size([]) == INVALID_INPUT)
assert(size({}) == INVALID_INPUT)
print("All is well (maybe!)")
