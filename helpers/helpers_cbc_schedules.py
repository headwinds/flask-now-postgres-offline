import json
# import pandas as pd
# import numpy as np
import requests
from bs4 import BeautifulSoup
# import time


def get_schedule(station):
    url = 'https://www.cbc.ca/programguide/daily/today/cbc_radio_one'
    urlParam = 'https://www.cbc.ca/programguide/daily/today/'+station
    print("url: ", urlParam)
    r = requests.get(urlParam)
    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find(id='sched-table')
    times = soup.find_all(class_='time')
    programs = soup.find_all(class_='program')

    count = 0
    schedule = []
    for program in programs:
        title = program.text.strip()
        start_time = times[count]["data-start-time"]
        end_time = times[count]["data-end-time"]
        program = {
            "title": title,
            "start-time": start_time,
            "end-time": end_time
        }
        schedule.append(program)
        # print("title: ", time)
        count += 1

    return schedule
