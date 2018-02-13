#!/usr/bin/python3

import requests

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

print(target)
print(headers)
r = requests.get(target, headers=headers)
print(r)
