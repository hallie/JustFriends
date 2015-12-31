import os, requests

###
# @function reformat_get_request_args
# @param {dict} ARGS - The arguments being passed to the URL request.
# @return reformat_args {string}
###
def reformat_get_request_args(ARGS):
    reformat_args = []
    # Loops through the args, in sorted order.
    for arg in sorted(ARGS.keys()):
        # Initializes a key_val string to "<lowercased key>=".
        key_val = arg.lower() + '='
        # If the value is a list, then join them.
        # Converts to string, just in case its lat/lon.
        if (type(ARGS[arg]) is list):
            key_val += ','.join(ARGS[arg])
        # Converts to a string if not a string.
        elif (type(ARGS[arg]) != str):
            key_val += str(ARGS[arg])
        # Just adds, as is, otherwise.
        else:
            key_val += ARGS[arg]
        # Appends the key_val to reformat_args
        reformat_args.append(key_val)
    # Combines all of the key_vals in reformat_args with an &.
    reformat_args = '&'.join(reformat_args)
    
    return reformat_args

###
# @function create_request_url
# @param {string} request_type
# @param {string} reformatted_args
# @return {string} PLACES_URL/Error_message
###
def create_request_url(request_type, reformatted_args):
    PLACES_URL = 'https://maps.googleapis.com/maps/api/place/'
    
    PLACE_REQUEST_TYPES = {
        'NEARBY': 'nearbysearch', # Lat/Lon, radius, opt=types, opt=name, key
        'DETAILS': 'details' # Only arg is placeid and API key
    }
    
    if (request_type in PLACE_REQUEST_TYPES):
        PLACES_URL += PLACE_REQUEST_TYPES[request_type]
        PLACES_URL += '/json?'
        PLACES_URL += reformatted_args
        PLACES_URL += ('&key=' + os.environ['GOOGLE_PLACES_API_KEY'])
        return PLACES_URL
        
        
    else:
        return "Error: Not Valid Request Type"

###
# @function request_response_json
# @param {string} REQUEST_URL - The url of the request to be sent.
# @return {json={}} RESPONSE_JSON - The request response object.
###
def request_response_json(REQUEST_URL):
    try:
        RESPONSE = requests.get(REQUEST_URL)
        RESPONSE_JSON = RESPONSE.json()
        return RESPONSE_JSON

    except requests.ConnectionError:
        print "Failed to Connect"
        return {}
