"""
Module to use google-maps-services-python in order to get geographic
information.

https://github.com/googlemaps/google-maps-services-python

$ pip install -U googlemaps
"""

import googlemaps
from numpy import nan

class GoogleMapsClient(object):

    def __init__(self, key):
        """Set client session with key
        https://developers.google.com/maps/documentation/geocoding/get-api-key
        """
        gmaps = googlemaps.Client(key)
        self.gmaps = gmaps

    def get_lat_lon_from_city_country(self, city, country, state=nan):
        """Returns latitude and longitude for a given city.

        Parameters
        ----------
        city : str
            City name.
        country : str
            Country name.
        state : str, opt
            State name.

        Returns
        -------
        location : tuple
            (latitude, longitude) in degs.
        """
        params = []
        if city is not nan:
            params.append(city)
        if state is not nan:
            params.append(state)
        if country is not nan:
            params.append(country)

        try:
            address = ", ".join(params)
        except TypeError:
            address = str(city)
            print(params)

        geocode_result = self.gmaps.geocode(address)

        try:
            location = geocode_result[0]['geometry']['location']
            lat = location['lat']
            lon = location['lng']
            result = (lat, lon)

        except IndexError:
            result = geocode_result
            print('wrong request: {}'.format(address))

        return result


if __name__ == '__main__':
    key = ''
    Session = GoogleMapsClient(key)

    cities = ['Coffs Harbour', 'Laverne', 'Roanoke']
    states = [None, 'OK', 'VA']
    countries = ['AS', 'USA', 'USA']

    answers = []

    for ii in range(3):
        loc = Session.get_lat_lon_from_city_country(cities[ii],
                                                         countries[ii],
                                                         states[ii])
        answers.append(loc)