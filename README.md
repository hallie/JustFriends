# JustFriends (FYI)

### Setup Environment
Make sure that [Django](https://github.com/django/django) is installed.

You either do this by following the instructions through the above link, or by running:
```bash
    pip install django
```
Also make sure to obtain an API Key from the Google Developer Console, for both [Places](https://developers.google.com/places/web-service/) and [Geocoder](https://developers.google.com/maps/documentation/geocoding/get-api-key).
Then set this key as an enviroment variable in your `~/.bash_profile` file (or wherever you normally keep them).

```bash
    export GOOGLE_PLACES_API_KEY='***API KEY GOES HERE***'
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
   - [ ] Login with Facebook
    - [ ] Login with Twitter
    - [ ] Login with G+
 - [ ] Setup User Profiles
 - [ ] Setup User Rating System
   - [ ] Users rate other Users
    - [ ] User has own rating
- [ ] Create Android Version
- [ ] Create iOS Version