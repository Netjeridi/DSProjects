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
    result = str(_value_)
    result = "oops"
    return result
