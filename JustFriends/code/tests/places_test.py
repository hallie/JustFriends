import sys, os, unittest

# Absolure path to the current test file.
TEST_FILE_PATH = os.path.abspath(__file__)
# The path to the test directory.
TEST_DIR = os.path.dirname(TEST_FILE_PATH)
# The path to the directory of the main code.
CODE_DIR = os.path.dirname(TEST_DIR)

# Appending the path to the main code to the sys path.
sys.path.append(CODE_DIR)


import places

class TestPlacesMethods(unittest.TestCase):

    def test_reformat_get_request_args_should_assert_equal(self):
        ARGS = {
            'LOCATION': ['37.600768', '-122.393177'],
            'RADIUS': 500,
            'TYPES': ['food'],
            'NAME': 'cruise'
        }
        
        expected_result  = "location=37.600768,-122.393177"
        expected_result += "&name=cruise"
        expected_result += "&radius=500"
        expected_result += "&types=food"

        returned_result = places.reformat_get_request_args(ARGS)
        
        self.assertEqual(returned_result, expected_result)
        
        
    def test_places_create_request_url_should_assert_equal(self):
        test_args = 'location=37.600768,-122.393177&types=food'
        
        expected_results  = 'https://maps.googleapis.com/maps/api/place/'
        expected_results += 'nearbysearch/json?' + test_args
        expected_results += '&key=' + os.environ['GOOGLE_PLACES_API_KEY']
        returned_results = places.create_request_url('NEARBY', test_args)
        
        self.assertEqual(expected_results, returned_results)
        
        
    def test_create_request_url_should_return_error_message(self):
        expected_results  = "Error: Not Valid Request Type"
        returned_results = places.create_request_url('FAKE_DATA', 'FAKE')
        
        self.assertEqual(expected_results, returned_results)
        
    
    def test_request_response_json_should_return_status_ok(self):
        REQUEST_URL  = 'https://maps.googleapis.com/maps/api/place/'
        REQUEST_URL += 'nearbysearch/json?location=37.600768,-122.393177'
        # TIL: Radius is a manditory param
        REQUEST_URL += '&radius=500&key=' + os.environ['GOOGLE_PLACES_API_KEY']
        
        expected_response = u'OK'
        
        returned_response = places.request_response_json(REQUEST_URL)
        if (u'status' in returned_response):
            returned_response = returned_response[u'status']
        
        self.assertEqual(expected_response, returned_response)
        

if __name__ == '__main__':
    unittest.main()