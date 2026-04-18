import pytest
from your_module import prime_factors

def test_prime_factors():
    assert prime_factors(10) == [2, 5]
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(17) == [17]
    assert prime_factors(1) == []
    assert prime_factors(0) == []
    assert prime_factors(-5) == [5]

def test_prime_factors_invalid_input():
    with pytest.raises(TypeError):
        prime_factors("10")
    with pytest.raises(TypeError):
        prime_factors(10.5)

def test_prime_factors_edge_cases():
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(5) == [5]
