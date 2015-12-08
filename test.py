import unittest
from tests.location_test import TestLocationMethods
from tests.places_test   import TestPlacesMethods
from tests.oauth_test    import TestOAuthMethods

if __name__ == '__main__':
    places_test_suite   = unittest.TestLoader().loadTestsFromTestCase(TestPlacesMethods)
    location_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLocationMethods)
    oauth_test_suite    = unittest.TestLoader().loadTestsFromTestCase(TestOAuthMethods)
    
    test_suite = [
        location_test_suite,
        places_test_suite,
        oauth_test_suite
    ]
    
    for suite in test_suite:
        unittest.TextTestRunner(verbosity=2).run(suite)