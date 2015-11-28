import requests, json, os

def get_current_geolocation_from_ip():
    GEOLOCATION_URL = 'http://freegeoip.net/json'
    RESPONSE = requests.get(GEOLOCATION_URL)
    RESPONSE_JSON = json.loads(RESPONSE.text)
    if (('latitude' in RESPONSE_JSON) and ('longitude' in RESPONSE_JSON)):
        lat = RESPONSE_JSON['latitude']
        lon = RESPONSE_JSON['longitude']
        return [str(lat), str(lon)]
    return [None, None]

def get_current_geolocation_from_address(address):
    GEOLOCATION_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
    address = address.split()
    address = '+'.join(address)
    GEOLOCATION_URL += ('address=' + address)
    GEOLOCATION_URL += ('&key=' + os.environ['GOOGLE_PLACES_API_KEY'])
    RESPONSE = requests.get(GEOLOCATION_URL)
    RESPONSE_JSON = json.loads(RESPONSE.text)
    if (u'results' in RESPONSE_JSON):
        RESPONSE_JSON = RESPONSE_JSON[u'results']
        if ((len(RESPONSE_JSON) > 0) and (u'geometry' in RESPONSE_JSON[0])):
            RESPONSE_JSON = RESPONSE_JSON[0][u'geometry']
            if (u'location' in RESPONSE_JSON):
                RESPONSE_JSON = RESPONSE_JSON[u'location']
                if ((u'lat' in RESPONSE_JSON) and (u'lng' in RESPONSE_JSON)):
                    lat = RESPONSE_JSON['lat']
                    lon = RESPONSE_JSON['lng']
                    return [str(lat), str(lon)]
    return [None, None]
    
#address = '2211 Mission Street, San Francisco, CA'
#returned = "u'location': {u'lat': 37.7615487, u'lng': -122.4191631}"
#print get_current_geolocation_from_address(address)