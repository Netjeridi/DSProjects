# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Levels of testing


# Unit Testing - testing at the function level


# Component Testing - testing at the library and compiled binary level


# System Testing - test the external interfaces of a system/collection of sub-systems


# Performance Testing - testing done at sub-system and system levels to verify timing,
# resource usage etc

# Simple Example

# Production Code
def str_len(the_str):
    """Example production code"""
    return len(the_str)

# A Unit Test


def test_string_length():
    """A basic example of a unit test"""
    test_str = "1"  # Setup - create the test string
    # Action - call production code to perform action
    result = str_len(test_str)
    assert result == 1  # Assert - validate the expected results of the action


test_string_length()

# Unit tests should be fast

# Test Driven Development (TDD) - workflow is broken up into 3 phases:
# - Red -- write a failing unit test
# - Green -- write just enough production code to make that test pass
# - Refactor -- refactor the unit test and production code to make it clean
# Repeat!

# 3 Laws of Agile software development and TDD
# - you may not write any production code until you have written a failing unit test
# - you may not write more of a unit test than is sufficient to fail, and not compiling is failing
# - you may not write more production code than is sufficient to pass the currently
# failing unit test


####################
# Example, can we write fizzbuzz code for 3x (fizz) 5x (buzz)

def fizz_buzz(_value_):
    if is_multiple(_value_, 3) and is_multiple(_value_, 5):
        result = "fizzbuzz"
    elif is_multiple(_value_, 3):
        result = "fizz"
    elif is_multiple(_value_, 5):
        result = "buzz"
    else:
        result = _value_
    return str(result)


def is_multiple(_value_, mod):
    return (_value_ % mod) == 0

######## TESTS ###########


def test_can_call_fizz_buzz():
    fizz_buzz(1)


def test_returns_1_with_1_passed_in():
    result = fizz_buzz(1)
    assert result == "1"


def test_returns_2_with_2_passed_in():
    result = fizz_buzz(2)
    assert result == "2"

# functionality between the two tests is duplicated, so refactor into a simple utility function


def check_fizz_buzz(_value_, expected_return_value):
    result = fizz_buzz(_value_)
    assert result == expected_return_value


def test_utility_returns_1_with_1_passed_in():
    check_fizz_buzz(1, "1")


def test_utility_returns_2_with_2_passed_in():
    check_fizz_buzz(2, "2")


def test_returns_fizz_with_3():
    check_fizz_buzz(3, "fizz")


def test_returns_buzz_with_5():
    check_fizz_buzz(5, "buzz")


def test_returns_fizz_with_factor_of_3():
    check_fizz_buzz(6, "fizz")


def test_returns_buzz_with_factor_of_5():
    check_fizz_buzz(10, "buzz")


def test_returns_fizzbuzz_with_15_passed():
    check_fizz_buzz(15, "fizzbuzz")
