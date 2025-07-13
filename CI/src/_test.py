import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth(n):
    return n**5

# testing the function
def test_sq():
    assert square(2) ==4, "Test Failed: the square of 2 must be 4"

def test_cube():
    assert cube(2) == 8, "Test Failed: the cube of 2 is 8"

def test_fifth():
    assert fifth(2)==32, "test failed: the fifth power of 2 is 32"

def test_invalid():
    with pytest.raises(TypeError):
        square("string")