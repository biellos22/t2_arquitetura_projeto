import pytest
from StringUtils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_reverse_string(string_utils):
    assert string_utils.reverse_string("abc") == "cba"
    assert string_utils.reverse_string("") == ""

def test_is_palindrome(string_utils):
    assert string_utils.is_palindrome("madam") is True
    assert string_utils.is_palindrome("hello") is False
    assert string_utils.is_palindrome("") is True

utils = StringUtils()
print(utils.reverse_string("hello"))  

utils = StringUtils()
print(utils.is_palindrome("LOL"))  
print(utils.is_palindrome("Arroz")) 
