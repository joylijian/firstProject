import pytest
import requests


def test_a():
    url = "https://energy-test.iotdataserver.net/api/realtimedata/records?$filter=deviceIdentifier%20eq%20SUBDEV16687494884830&queryType=2&collectTime=1661961600000&queryDirection=4&querySize=1000&recordType=2"

    payload = {}
    headers = {
        'Authorization': 'bearer NmNiYzdkZTItNTNkMS00MjkzLWJkMDQtNzM1MjY5ZDFlZDJm',
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'energy-test.iotdataserver.net',
        'Connection': 'keep-alive'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200

    print(response.json())
    # list1 = response.json()['data']
    # n = 0
    # for item in list1:
    #     n = n + 1
    #
    # # print(type(list1))
    # # print(type(response.json()))
    # # print(response.json())
    # ids = []
    # for i in range(0, n):
    #     deviceId = response.json()['data'][i]['id']
    #     ids.append(deviceId)


if __name__ == '__main__':
    pytest.main(['-s', '-vv', 'test_mypy.py', '--alluredir', './report/xml'])
