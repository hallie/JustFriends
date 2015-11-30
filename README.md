# JustFriends (FYI) [![Build Status](https://travis-ci.org/rhallie15/JustFriends.svg?branch=master)](https://travis-ci.org/rhallie15/JustFriends)

### Setup Environment
Make sure that [Django](https://github.com/django/django) and [Django Rest Framework](https://github.com/tomchristie/django-rest-framework) are installed.

You either do this by following the instructions through the above links, or by running:
```bash
    pip install -r requirements.txt
```
Also make sure to obtain an API Key from the Google Developer Console, for both [Places](https://developers.google.com/places/web-service/) and [Geocoder](https://developers.google.com/maps/documentation/geocoding/get-api-key).
Then set this key as an enviroment variable in your `~/.bash_profile` file (or wherever you normally keep them).

```bash
    export GOOGLE_PLACES_API_KEY='***API KEY GOES HERE***'
```

To use the OAuth features, you'll need API keys and secrets from [Twitter](https://apps.twitter.com/), [Facebook](https://developers.facebook.com/apps/), and [Google+](https://developers.google.com/+/web/api/rest/oauth).

```bash
    export JF_TWITTER_API_KEY='***API KEY GOES HERE***'
    export JF_TWITTER_API_SECRET='***API SECRET GOES HERE***'
    
    export JF_FACEBOOK_API_KEY='***API KEY GOES HERE***'
    export JF_FACEBOOK_API_SECRET='***API SECRET GOES HERE***'
    
    export JF_GOOGLEPLUS_API_KEY='***API KEY GOES HERE***'
    export JF_GOOGLEPLUS_API_SECRET='***API SECRET GOES HERE***'
```

Don't forget the [Django Secret Key](http://www.miniwebtool.com/django-secret-key-generator/)! (I know I almost did)
```bash
    export JUSTFRIENDS_APP_SECRET='***SECRET KEY GOES HERE***'
```

Then make sure to migrate the database tables.
```bash
    python manage.py migrate
```

### Start Project
```bash
    python manage.py runserver 8080
```

### Run UnitTests
```bash
    python tests.py
```
    
### TODO:
- [ ] Setup Location Data
 - [x] Get Geolocation from Address
 - [x] Get Places Nearby by Geolocation
 - [ ] Map Google Places to Yelp Listings
- [ ] Create User DB
 - [ ] Setup OAuth
   - [ ] Login with Facebook :blue_book:
    - [ ] Login with Twitter :bird:
    - [ ] Login with G+ :see_no_evil: :speak_no_evil: :hear_no_evil:
 - [ ] Setup User Profiles
 - [ ] Setup User Rating System
   - [ ] Users rate other Users
    - [ ] User has own rating
- [ ] Create Android Version :pager:
- [ ] Create iOS Version :iphone:
