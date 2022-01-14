
import requests

if __name__ == '__main__':
    print(requests.__version__)

    print(requests.get('http://google.com/'))

    url = 'https://raw.githubusercontent.com/waseemyusuf/cmput404_lab1/main/script.py'
    print(requests.get(url).text)

