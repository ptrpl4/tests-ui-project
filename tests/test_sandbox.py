import pytest


# --------------------------------------------------------------------------------
# A test function that triggers an exception
# --------------------------------------------------------------------------------
def test_divide_by_zer0():
    num = 1 / 0
    return num


# --------------------------------------------------------------------------------
# A test function that verifies an exception
# --------------------------------------------------------------------------------
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)
