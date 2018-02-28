#!/usr/bin/python3

import requests
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

r = requests.get(target, headers=headers)


def get_value_from_object_with_key(obj, key):

    return obj['response']['data']['METAR'][key]


r = requests.get(target, headers=headers)

if r.status_code == 200:
    obj = xmltodict.parse(r.text)
else:
    print('Response code is {}'.format(r))

result = get_value_from_object_with_key(obj, 'temp_c')
print('The temp is {} celsius, '
      'which is {} fahrenheit'.format(result, (float(result) * (9/5) + 32)))
