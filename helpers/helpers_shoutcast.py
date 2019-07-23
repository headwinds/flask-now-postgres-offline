import json
# import pandas as pd
# import numpy as np
import requests
from bs4 import BeautifulSoup
# import time

get shoutcast_url(station):
    return ""


def get_shoutcast(station):
    urlParam = 'https://www.cbc.ca/programguide/daily/today/'+station
    response = requests.get(urlParam)
    if response.status_code == 200:
        print('Success!')
        return response.json()
    elif response.status_code == 404:
        print('Not Found.')

    