import requests


def get_location_info():
    return requests.get('http://api.ipstack.com/check?access_key=ba6e1e62f1b4fc39908f03182ed91a9d&format=1').json()
    # my_free_api_key = ba6e1e62f1b4fc39908f03182ed91a9d


print(get_location_info())
