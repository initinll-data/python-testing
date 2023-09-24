import unittest

from phonebook.phonebook_processor_unittest import Phonebook

# run tests: python -m unittest

# testing using unittest
# declare a class containing tests


class PhonebookTest(unittest.TestCase):

    # setup a fixture method
    # special method (test fixture), gets called before every test case is executed
    def setUp(self) -> None:
        self.phonebook = Phonebook()

    # tear down fixture method
    # used to release any resource tied up in setup method
    def tearDown(self) -> None:
        pass

    # test cases -
    # first test case
    def test_lookup_by_name(self):
        # arrange
        self.phonebook.add("bob", "1234")
        # act
        number = self.phonebook.lookup("bob")
        # assert
        self.assertEqual(number, "1234")

    # second test case
    def test_missing_name(self):
        # act & assert
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # third test case
    def test_empty_phonebook_is_consistent(self):
        # act
        is_consistent = self.phonebook.is_consistent()
        # assert
        self.assertTrue(is_consistent)

    # fourth test case
    def test_is_consistent_with_different_entries(self):
        # arrange
        self.phonebook.add("bob", "1234")
        self.phonebook.add("anna", "6789")
        # act
        is_consistent = self.phonebook.is_consistent()
        # assert
        self.assertTrue(is_consistent)

    # fifth test case
    def test_inconsistent_with_duplicate_entries(self):
        # arrange
        self.phonebook.add("bob", "1234")
        self.phonebook.add("sue", "1234")  # identical to bob
        # act
        is_consistent = self.phonebook.is_consistent()
        # assert
        self.assertFalse(is_consistent)

    # sixth test case
    def test_inconsistent_with_duplicate_prefix(self):
        # arrange
        self.phonebook.add("bob", "1234")
        self.phonebook.add("sue", "123")
        # act
        is_consistent = self.phonebook.is_consistent()
        # assert
        self.assertFalse(is_consistent)
