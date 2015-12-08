import unittest, test_helper

import oauth.oauth_helper as oa_help

class TestOAuthMethods(unittest.TestCase):
    def test_get_api_key_should_return_string_for_twitter(self):
        test_api_name = 'twitter'
        
        returned_result = oa_help.get_api_key(test_api_name)
        expected_result = (type(returned_result) == str)
        
        self.assertTrue(expected_result)
    
    def test_get_api_secret_should_return_string_for_twitter(self):
        test_api_name = 'twitter'
        
        returned_result = oa_help.get_api_secret(test_api_name)
        expected_result = (type(returned_result) == str)
        
        self.assertTrue(expected_result)
        
    def test_get_api_key_should_return_string_for_google(self):
        test_api_name = 'googleplus'
        
        returned_result = oa_help.get_api_key(test_api_name)
        expected_result = (type(returned_result) == str)
        
        self.assertTrue(expected_result)
    
    def test_get_api_secret_should_return_string_for_google(self):
        test_api_name = 'googleplus'
        
        returned_result = oa_help.get_api_secret(test_api_name)
        expected_result = (type(returned_result) == str)
        
        self.assertTrue(expected_result)
        
    def test_get_api_key_should_return_string_for_facebook(self):
        test_api_name = 'facebook'
        
        returned_result = oa_help.get_api_key(test_api_name)
        expected_result = (type(returned_result) == str)
        
        self.assertTrue(expected_result)
    
    def test_get_api_secret_should_return_string_for_facebook(self):
        test_api_name = 'facebook'
        
        returned_result = oa_help.get_api_secret(test_api_name)
        expected_result = (type(returned_result) == str)
        
        self.assertTrue(expected_result)
    
if __name__ == '__main__':
    unittest.main()