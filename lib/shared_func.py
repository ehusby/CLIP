
from lib import base_func


def connected_to_internet():
    try:
        import httplib
    except ImportError:
        import http.client as httplib

    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception:
        conn.close()
        return False


def geo_get_epsg_code():
    epsg = base_func.get_user_input("EPSG code: ").strip()
    try:
        epsg = int(epsg)
    except ValueError:
        raise base_func.ClipInputError("EPSG code must be an integer")
    return epsg


def geo_parse_coords(coords):
    import re

    coords_list = re.findall(r"-?\d+\.?\d*", coords, flags=re.MULTILINE)
    if len(coords_list) != 2:
        raise base_func.ClipInputError(
            "Failed to parse two coordinate values from clipboard"
        )

    return coords_list


def geo_address_to_coords(address, coord_axis_order=('lat', 'lon')):
    import json
    import operator
    import urllib.parse
    import urllib.request

    if not connected_to_internet():
        raise base_func.ClipLookupError("Internet connection is required to lookup addresses")

    address = address.strip()

    lookup_url = r'https://nominatim.openstreetmap.org/search?&format=json&limit=1&polygon=0&addressdetails=0&email=intellij.geocoding.plugin@gmail.com&q={}'.format(
        urllib.parse.quote(f'"{address}"')
    )
    try:
        with urllib.request.urlopen(lookup_url) as response:
            address_json = json.loads(response.read().decode())
    except:
        print(f"Lookup URL: {lookup_url}")
        raise

    latlon_string = ','.join(operator.itemgetter(*coord_axis_order)(address_json[0]))
    return latlon_string


def geo_coords_to_address(coords, coord_axis_order=('lat', 'lon')):
    import json
    import urllib.request

    if not connected_to_internet():
        raise base_func.ClipLookupError("Internet connection is required to lookup addresses")

    address_json_displayname_key = 'display_name'

    coords_list = geo_parse_coords(coords)
    coords_dict = dict(zip(coord_axis_order, coords_list))

    lookup_url = r'https://nominatim.openstreetmap.org/reverse?&format=json&limit=1&addressdetails=0&accept-language=en&zoom=10&email=intellij.geocoding.plugin@gmail.com&lon={}&lat={}'.format(
        coords_dict['lon'], coords_dict['lat']
    )
    try:
        with urllib.request.urlopen(lookup_url) as response:
            address_json = json.loads(response.read().decode())
    except:
        print(f"Lookup URL: {lookup_url}")
        raise

    if address_json_displayname_key not in address_json:
        print(f"Lookup URL: {lookup_url}")
        print(f"JSON data: {address_json}")
        raise base_func.ClipLookupError(f"Address string key '{address_json_displayname_key}' not found in JSON data")

    address_string = address_json[address_json_displayname_key]
    return address_string
