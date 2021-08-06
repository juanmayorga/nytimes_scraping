import requests
import lxml.html as html
HOME_URL = 'https://www.nytimes.com'

XPATH_LINKS = '//div[@class="css-1l4spti"]/a/@href'
XPATH_TITLE = '//h1[@class="css-v3w0l4 e1h9rw200"]/text()'
XPATH_SUMMARY = '//h1[@class="css-v3w0l4 e1h9rw200"]/text()'
XPATH_BODY = '//h1[@class="css-v3w0l4 e1h9rw200"]/text()'


def parse_home():
    try:
        pass
    except ValueError as e:
        print(e)


def run():
    parse_home()


if __name__ = '__main__':
    run()
