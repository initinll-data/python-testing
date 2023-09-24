
# test fixture / setup
import pytest

from phonebook.phonebook_processor_pytest import PhonebookMaker

# TThe fixture function is kept here into a separate conftest.py file so that tests from multiple test modules in the directory can access the fixture function
# refer - https://docs.pytest.org/en/6.2.x/fixture.html
# multiple fixtures can be stored here


@pytest.fixture
def phonebook_maker_resource(tmpdir):
    "Provides an empty PhonebookMaker"
    # return resource
    # return Phonebook()
    # to tear down yield instead of return which means the the code after yield wil be executed after the execution of test case
    # yielding resource
    phonebook_maker = PhonebookMaker(tmpdir)
    yield phonebook_maker
    # teardown after test case execution
    phonebook_maker.clear()
