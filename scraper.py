import re
import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.nytimes.com/es'

XPATH_LINKS = '//div[@class="css-1l4spti"]/a/@href'
XPATH_TITLE = '//h1[@class="css-v3w0l4 e1h9rw200" or @class="css-1w1syaa e1h9rw200" or @class="css-15m43iq e1h9rw200" or @class="css-hzs6w4 e1h9rw200" or @class="css-rsa88z e1h9rw200"]/text()'
XPATH_SUMMARY = '//p[@class="css-1kg93su e1wiw3jv0" or @class="css-1b6a17a e1wiw3jv0" or @class="css-w6ymp8 e1wiw3jv0" or @class="css-w6ymp8 e1wiw3jv0"]/text()'
XPATH_BODY = '//p[@class="css-axufdj evys1bk0"]/text()'


def parse_news(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            news = response.content.decode('utf-8')
            parsed = html.fromstring(news)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                title = title.replace('‘', '')
                title = title.replace('’', '')
                title = title.replace(':', '')
                title = title.replace('¿', '')
                title = title.replace('?', '')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as e:
        print(e)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        urlhome = HOME_URL
        urlhome = urlhome.replace("/es", "")

        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINKS)
            # print(urlhome+links)
            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
            for link in links:
                # print(urlhome+link)
                parse_news(urlhome+link, today)

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as e:
        print(e)


def run():
    parse_home()


if __name__ == '__main__':
    run()
