import requests, json, os

###
# TODO: Find a better geolocator API (issues/5)
###
def get_current_geolocation_from_ip():
    GEOLOCATION_URL = 'http://freegeoip.net/json'
    RESPONSE = requests.get(GEOLOCATION_URL)
    RESPONSE_JSON = json.loads(RESPONSE.text)
    if (('latitude' in RESPONSE_JSON) and ('longitude' in RESPONSE_JSON)):
        lat = RESPONSE_JSON['latitude']
        lon = RESPONSE_JSON['longitude']
        return [str(lat), str(lon)]
    return [None, None]

###
# @function get_current_geolocation_from_address
# @param {string} address - The address of the user's location.
# @return {list=[None, None]} [LAT, LON] - List containing the Lat/Lon values. 
###
def get_current_geolocation_from_address(address):
    # Base URL for Google Geocode API
    GEOLOCATION_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
    
    # Replaces spaces with '+' in passed address string.
    address = address.replace(' ', '+')
    
    # Adds the address and api key to the request url.
    GEOLOCATION_URL += ('address=' + address)
    GEOLOCATION_URL += ('&key=' + os.environ['GOOGLE_PLACES_API_KEY'])
    
    # Sets the returned object to the RESPONSE variable.
    RESPONSE = requests.get(GEOLOCATION_URL)
    RESPONSE_JSON = json.loads(RESPONSE.text).get('results')
    
    # Initializes the Lat/Lon values to None
    LAT = LON = None
    
    # If the length of the results is greater than zero, attempts to get the lat/lon
    if ((RESPONSE_JSON != None) and (len(RESPONSE_JSON) > 0)):
        RESPONSE_JSON = RESPONSE_JSON[0].get('geometry').get('location')
        LAT = str(RESPONSE_JSON.get('lat'))
        LON = str(RESPONSE_JSON.get('lng'))
    
    return [LAT, LON]
