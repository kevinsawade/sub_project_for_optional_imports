import unittest
from import_sub_project import print_hello_user
import getpass

class TestPrintHelloUser(unittest.TestCase):
    def test_function(self):
        returned_message = print_hello_user()
        shouldbe_message = f"Hello {getpass.getuser()}!"
        self.assertEqual(returned_message, shouldbe_message)

test_cases = (TestPrintHelloUser, )
import doctest
from import_sub_project import phum
doc_tests = (doctest.DocTestSuite(phum), )

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        filtered_tests = [t for t in tests if not t.id().endswith('.test_session')]
        suite.addTests(filtered_tests)
    suite.addTests(doc_tests)
    return suite
