#!/usr/bin/python3

import requests
import json
import xmltodict

dsource = 'metars'
station = 'KPSC'
hoursbefore = '1'
dformat = 'xml'

target = (
      'https://aviationweather.gov'
      '/adds/dataserver_current/httpparam'
      '?dataSource={0}'
      '&requestType=retrieve'
      '&format={1}'
      '&stationString={2}'
      '&hoursBeforeNow={3}'
      .format(dsource, dformat, station, hoursbefore)
      )


headers = {
       'User-Agent':
       ('Mozilla/5.0 (X11; Linux x86_64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/52.0.2743.82 Safari/537.36')
       }

# print(target)
# print(headers)
r = requests.get(target, headers=headers)
# print(r)
# print(r.text)

if r.status_code == 200:
    obj = xmltodict.parse(r.text)
else:
    print('Response code is {}'.format(r))

# print(json.dumps(obj, indent=4, sort_keys=True))
# print(obj['response']['data']['METAR']['observation_time'])
# print(obj['response']['data']['METAR']['station_id'])
# print(obj['response']['data']['METAR']['temp_c'])

for key, value in obj['response']['data']['METAR'].items():
    print(key, value)
