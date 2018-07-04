import requests
from requests.exceptions import RequestException
import json


def get_one_page_index(offset, keyword):
    para = {'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
            'from': 'search_tab'}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
    }
    try:
        response = requests.get('https://www.toutiao.com/search_content/', params=para, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
    except RequestException:
        print('请求出错')


def parser(html):
    # print(type(html))
    html = json.loads(html)

    return {data.get('title'):data.get('share_url') for data in html['data']}


def main():
    html = get_one_page_index(0, '街拍')
    data_list = parser(html)
    for data in data_list:
        if data:
            print(data+': '+data_list[data])
            print('--------')


if __name__ == '__main__':
    main()
