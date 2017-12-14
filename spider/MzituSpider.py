import os

from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.mzitu.com/all/'
download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mzitu')
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
}
if not os.path.exists(download_dir):
    os.mkdir(download_dir)


def _html(url):
    return requests.get(url, headers=headers).text


def get_internal_links(html):
    return BeautifulSoup(html, 'lxml').find('div', {'class': 'all'}).findAll('a')


def download_image(url):
    print('downloading =========>', url)
    src = BeautifulSoup(_html(url), 'lxml').find('div', {'class': 'main-image'}).find('img')['src']
    filename = '{}/{}'.format(download_dir, src[-9:])
    print('filename ====================>', filename.split('/')[-1])
    headers['referer'] = url
    with open(filename, 'wb') as fp:
        fp.write(requests.get(src, headers=headers).content)


def download_images(href, desc):
    print('will download  ==========================', desc, '==========================')
    total = BeautifulSoup(_html(href), 'lxml').find('div', {'class': 'pagenavi'}).findAll('span')[-2].get_text()
    headers['referer'] = href
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(download_image, map(lambda index: '{}/{}'.format(href, index), range(1, int(total) + 1)))


def start():
    html = _html(base_url)
    links = get_internal_links(html)
    for link in links:
        href, desc = link['href'], link.get_text()
        download_images(href, desc)


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as e:
        pass
