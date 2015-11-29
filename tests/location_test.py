import unittest, test_helper

import places_to_go.location as loc

class TestLocationMethods(unittest.TestCase):
    def test_get_current_geolocation_from_address_should_assert_equal(self):
        test_address = '2211 Mission Street, San Francisco, CA'
        
        expected_result = ['37.7615487', '-122.4191631']
        returned_result = loc.get_current_geolocation_from_address(test_address)
        
        self.assertEqual(returned_result, expected_result)
    
if __name__ == '__main__':
    unittest.main()