def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

import pytest

def test_all_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0
    assert count_vowels("123!@#") == 0

def test_mixed_string():
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 4
    assert count_vowels("aEiOu123bcd") == 5

def test_empty_string():
    assert count_vowels("") == 0