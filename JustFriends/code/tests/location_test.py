import sys, os, unittest

# Absolure path to the current test file.
TEST_FILE_PATH = os.path.abspath(__file__)
# The path to the test directory.
TEST_DIR = os.path.dirname(TEST_FILE_PATH)
# The path to the directory of the main code.
CODE_DIR = os.path.dirname(TEST_DIR)

# Appending the path to the main code to the sys path.
sys.path.append(CODE_DIR)


import location

class TestLocationMethods(unittest.TestCase):
    def test_get_current_geolocation_from_address_should_assert_equal(self):
        test_address = '2211 Mission Street, San Francisco, CA'
        
        expected_result = ['37.7615487', '-122.4191631']
        returned_result = location.get_current_geolocation_from_address(test_address)
        
        self.assertEqual(returned_result, expected_result)
    
if __name__ == '__main__':
    unittest.main()