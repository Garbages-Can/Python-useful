import os

from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


class MzituSpider:
    base_url = 'http://www.mzitu.com/all/'
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mzitu')
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

    def __init__(self):
        if not os.path.exists(self.download_dir):
            os.mkdir(self.download_dir)

    def _html(self, url):
        return requests.get(url, headers=self.headers).text

    def get_internal_links(self, html):
        return BeautifulSoup(html, 'lxml').find('div', {'class': 'all'}).findAll('a')

    def download_image(self, url):
        print('downloading =========>', url)
        src = BeautifulSoup(self.html(url), 'lxml').find('div', {'class': 'main-image'}).find('img')['src']
        filename = '{}/{}'.format(self.download_dir, src[-9:])
        print('filename ====================>', filename.split('/')[-1])
        self.headers['referer'] = url
        with open(filename, 'wb') as fp:
            fp.write(requests.get(src, headers=self.headers).content)

    def download_images(self, href, desc):
        print('will download  ==========================', desc, '==========================')
        total = BeautifulSoup(self.html(href), 'lxml').find('div', {'class': 'pagenavi'}).findAll('span')[-2].get_text()
        self.headers['referer'] = href
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            executor.map(self.download_image, map(lambda index: '{}/{}'.format(href, index), range(1, int(total) + 1)))

    def start(self):
        html = self.html(self.base_url)
        links = self.get_internal_links(html)
        for link in links:
            href, desc = link['href'], link.get_text()
            self.download_images(href, desc)


if __name__ == '__main__':
    spider = MzituSpider()
    spider.start()
