import os


VALID_APIS = set(['facebook', 'googleplus', 'twitter'])

def get_api_key(api_type):
    if (api_type.lower() in VALID_APIS):
        api_key_name = 'JF_{}_API_KEY'.format(api_type.upper())
        try:
            return os.environ[api_key_name]
        except KeyError:
            print "Did you remember to set the key for {}?".format(api_type)
    return None

def get_api_secret(api_type):
    if (api_type.lower() in VALID_APIS):
        api_secret_name = 'JF_{}_API_SECRET'.format(api_type.upper())
        try:
            return os.environ[api_secret_name]
        except KeyError:
            print "Did you remember to set the secret for {}?".format(api_type)
    return None