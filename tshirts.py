INVALID_INPUT = 'Invalid input'

def size(cms):
    """Returns clothing size based on chest measurement in cms."""
    if not isinstance(cms, (int, float)) or cms < 0:
        return INVALID_INPUT
    if cms < 38:
        return 'S'
    elif cms < 42:
        return 'M'
    return 'L'

# Test cases
def test_size():
    # Valid inputs
    assert size(37) == 'S'
    assert size(0) == 'S'      
    assert size(38) == 'M'    
    assert size(40) == 'M'
    assert size(41.9) == 'M'   
    assert size(42) == 'L'      
    assert size(43) == 'L'
    assert size(100) == 'L'    

    # Invalid inputs
    assert size(-1) == INVALID_INPUT
    assert size('abc') == INVALID_INPUT
    assert size(None) == INVALID_INPUT
    assert size([]) == INVALID_INPUT
    assert size({}) == INVALID_INPUT
    assert size(True) == INVALID_INPUT  

    print("All tests passed successfully.")

test_size()
