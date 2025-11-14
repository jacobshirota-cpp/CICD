import main
import pytest

def test_one():
    num = main.add(3, 4)
    num = main.subtract(num, 5)
    num = main.multiply(num, 8)
    assert num == 16

