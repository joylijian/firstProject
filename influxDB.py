from influxdb import InfluxDBClient
import requests

from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS

if __name__ == '__main__':
    token = "EWdx8x3mmzQxVGf8f573kBGBvSv0iIK97YJMJIqgeb_J5LZKfm-qpxF2lKDS4R0ImtdzSyChiCUx1fI-Cz_dwA=="
    org = "orgs"
    bucket = "iem"

    client = InfluxDBClient(url="http://10.44.219.28:8086", token=token, org=org, )

    # write_api = client.write_api(write_options=SYNCHRONOUS)
    # query_api = client.query_api()

    sql = "SELECT value FROM table1"
    result = client.get_list_measurements()
    print(result)
    result1 = client.query(sql)
    print(result1)
    # print(list(client.query(sql).get_points()))
    client.close()

# if __name__ == '__main__':
#     host, port = "10.44.219.28", 8086
#     username, password = "root", "inovance123"
#     database = "iem"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#         'Accept': '*/*',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json'
#         # 'authorization': 'Basic cm9vdDppbm92YW5jZTEyMw=='
#     }
#     client = InfluxDBClient(host=host, username=username, port=port, database=database, password=password,
#                             headers=headers)
#     sql = "SELECT value FROM table1"
#     # print(list(client.query(sql).get_points()))
#     client.close()
