import sys

import pytest

from phonebook.phonebook_processor_pytest import PhonebookMaker

# run tests: pytest -rA

# fixture - phonebook_maker_resource is configured in special file - conftest.py
# tests from multiple test modules in the directory can access the fixture function automatically due to this special file
# set name of fixture method name as argument to test method

# test case 1


def test_lookup_by_name(phonebook_maker_resource):
    # arrange
    expected_value = "1234"
    # act
    phonebook_maker_resource.add("bob", "1234")
    actual_value = phonebook_maker_resource.lookup("bob")
    # assert
    assert actual_value == expected_value

# test case 2


def test_contains_all_names(phonebook_maker_resource):
    # arrange
    expected_values = {"bob"}
    # act
    phonebook_maker_resource.add("bob", "1234")
    actual_values = phonebook_maker_resource.all_names()
    # assert
    assert actual_values == expected_values

# test case 3


def test_missing_name(phonebook_maker_resource):
    # arrange
    # phonebook_maker_resource.add("bob", "1234")
    # act & assert
    with pytest.raises(KeyError):
        phonebook_maker_resource.lookup("bob")

# test case 4


def test_empty_phonebook_is_consistent(phonebook_maker_resource):
    # act
    expected_value = True
    actual_value = phonebook_maker_resource.is_consistent()
    # assert
    assert actual_value is expected_value

# test case 5


def test_is_consistent_with_different_entries(phonebook_maker_resource):
    # arrange
    phonebook_maker_resource.add("bob", "1234")
    phonebook_maker_resource.add("anna", "6789")
    expected_value = True
    # act
    actual_value = phonebook_maker_resource.is_consistent()
    # assert
    assert actual_value is expected_value

# test case 6


def test_inconsistent_with_duplicate_entries(phonebook_maker_resource):
    # arrange
    phonebook_maker_resource.add("bob", "1234")
    phonebook_maker_resource.add("sue", "1234")  # identical to bob
    expected_value = False
    # act
    actual_value = phonebook_maker_resource.is_consistent()
    # assert
    assert actual_value is expected_value

# test case 7


def test_inconsistent_with_duplicate_prefix(phonebook_maker_resource):
    # arrange
    phonebook_maker_resource.add("bob", "1234")
    phonebook_maker_resource.add("sue", "123")
    expected_value = True
    # act
    actual_value = phonebook_maker_resource.is_consistent()
    # assert
    assert actual_value is not expected_value

# test case 8 - converting test cases 5,6 & 7 into parameterrized tests due to common body
# "test_value1,test_value2,expected_value" should match -> (phonebook_maker_resource, test_value1, test_value2, expected_value)


@pytest.mark.parametrize(
    "test_value1,test_value2,expected_value", [
        (("bob", "1234"), ("anna", "6789"), True),  # 5 test case
        (("bob", "1234"), ("sue", "1234"), False),  # 6 test case
        (("bob", "1234"), ("sue", "123"), False)  # 7 test case
    ]
)
def test_is_consistent(phonebook_maker_resource, test_value1, test_value2, expected_value):
    # arrange
    phonebook_maker_resource.add(*test_value1)
    phonebook_maker_resource.add(*test_value2)
    # act
    actual_value = phonebook_maker_resource.is_consistent()
    # assert
    assert actual_value is expected_value


# test case 9
# deselect this test by: pytest -m "not slow" (to skip only this test)
# select this test by: pytest -m "slow" (to run only this test)
# this is custom marker configured in pyproject.toml file under [tool.pytest.ini_options]

@pytest.mark.slow
def test_dummy_slow_test():
    pass

# test case 10
# deselect this test by: pytest -m "not serial" (to skip only this test)
# select this test by: pytest -m "serial" (to run only this test)
# this is custom marker configured in pyproject.toml file under [tool.pytest.ini_options]


@pytest.mark.serial
def test_dummy_serial_test():
    pass

# test case 11
# using built-in marker skip (to skip the test)
# more info - pytest --markers
# this tests automatically gets skipped from running


@pytest.mark.skip("Work in progress")
def test_dummy_skip1_test():
    pass


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_dummy_skip2_test():
    pass
