
from lib import base_func


def geo_address_to_coords(address, coord_axis_order=('lat', 'lon')):
    import json
    import operator
    import urllib.parse
    import urllib.request

    address = address.strip()

    lookup_url = r'https://nominatim.openstreetmap.org/search?&format=json&limit=1&polygon=0&addressdetails=0&email=intellij.geocoding.plugin@gmail.com&q={}'.format(
        urllib.parse.quote('"{}"'.format(address))
    )
    try:
        with urllib.request.urlopen(lookup_url) as response:
            address_json = json.loads(response.read().decode())
    except:
        print("Lookup URL: {}".format(lookup_url))
        raise

    latlon_string = ','.join(operator.itemgetter(*coord_axis_order)(address_json[0]))
    return latlon_string


def geo_coords_to_address(coords, coord_axis_order=('lat', 'lon')):
    import json
    import re
    import urllib.request

    coords_pattern = ".*?(-?\d+\.?\d*).*?[\r\n]*(-?\d+\.?\d*).*?"
    address_json_displayname_key = 'display_name'

    clip_contents = coords.strip()
    match = re.search(coords_pattern, clip_contents, re.MULTILINE)
    if match is None:
        raise base_func.ClipSyntaxError(
            "Failed to parse lat/lon coordinates from clipboard using regex: {}".format(coords_pattern)
        )
    coords_tuple = match.groups()

    coords_dict = dict(zip(coord_axis_order, coords_tuple))

    lookup_url = r'http://nominatim.openstreetmap.org/reverse?&format=json&limit=1&addressdetails=0&accept-language=en&zoom=10&email=intellij.geocoding.plugin@gmail.com&lon={}&lat={}'.format(
        coords_dict['lon'], coords_dict['lat']
    )
    try:
        with urllib.request.urlopen(lookup_url) as response:
            address_json = json.loads(response.read().decode())
    except:
        print("Lookup URL: {}".format(lookup_url))
        raise

    if address_json_displayname_key not in address_json:
        print("Lookup URL: {}".format(lookup_url))
        print("JSON data: {}".format(address_json))
        raise base_func.ClipLookupError("Address string key '{}' not found in JSON data".format(address_json_displayname_key))

    address_string = address_json[address_json_displayname_key]
    return address_string
