import unittest
from JustFriends.code.tests.location_test import TestLocationMethods
from JustFriends.code.tests.places_test import TestPlacesMethods

if __name__ == '__main__':
    places_test_suite   = unittest.TestLoader().loadTestsFromTestCase(TestPlacesMethods)
    location_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLocationMethods)
    
    test_suite = [
        location_test_suite,
        places_test_suite
    ]
    
    for suite in test_suite:
        unittest.TextTestRunner(verbosity=2).run(suite)