import pytest
from FibonacciGenerator import FibonacciGenerator

@pytest.fixture
def fib_generator():
    return FibonacciGenerator()

def test_generate_sequence_empty(fib_generator):
    assert fib_generator.generate_sequence(0) == []
    assert fib_generator.generate_sequence(-1) == []

def test_generate_sequence_normal(fib_generator):
    assert fib_generator.generate_sequence(1) == [0]
    assert fib_generator.generate_sequence(5) == [0, 1, 1, 2, 3]

def test_get_nth_number_invalid(fib_generator):
    assert fib_generator.get_nth_number(0) is None
    assert fib_generator.get_nth_number(-1) is None

def test_get_nth_number_valid(fib_generator):
    assert fib_generator.get_nth_number(1) == 0
    assert fib_generator.get_nth_number(2) == 1
    assert fib_generator.get_nth_number(6) == 5

generator = FibonacciGenerator()
print(generator.generate_sequence(15)) 

generator = FibonacciGenerator()
print(generator.get_nth_number(6)) 
