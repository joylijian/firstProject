import requests
import json


def get_yunxing():
    url = "https://energy-test.iotdataserver.net/api/compdata/datalinks?$filter=status%20eq%201&pagination=0&inherit=custom"

    payload = json.dumps({
        "linkIds": [
            "1595659699594858496"
        ],
        "params": {
            "1": 1,
            "page": "1",
            "pageCount": "10",
            "startTime": "2022-11-30T00:00:00Z",
            "endTime": "2022-11-30T01:00:00Z",
            "pageSize": 10
        }
    })
    headers = {
        'Authorization': 'bearer NTg2MjdjNjgtNjE0Zi00NDdlLThkZDctMTcwNDU1YjYxZWE0',
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': 'energy-test.iotdataserver.net',
        'Connection': 'keep-alive',
        'Cookie': 'eid=afaf242412fasf;x-xscf-token=wqreefafasf1111'
    }

    session = requests.Session()
    r = session.post(url, headers=headers, data=payload)
    r.cookies.set('eid', '2235wtwttwt')
    r.cookies.set('x-xcsf-token', '25252ggsdt')
    request_cookies = session.cookies.get_dict()
    # print(request_cookies)  #可以打印出来看下有没有获取到
    # return request_cookies
    ck = r.cookies
    zi = {}
    print(ck)
    print(ck.keys())
    print(ck.values())


    # for item in list(r.cookies):
    #     print(item.k)
    #     print(type(item))
    # print(r.cookies)
    # print(r.text)

    # response = .request("POST", url, headers=headers, data=payload)

    # cookies = response.cookies.items()
    # print(cookies)
    #
    # print(response.text)


get_yunxing()
