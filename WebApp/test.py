import geocoder

def get_country_code():
    # Get your current IP-based location
    g = geocoder.ip('me')
    # Return the country code
    return g.geojson['features'][0]['properties']['country']

country_code = get_country_code()
print("Country Code:", country_code)
