from dataclasses import dataclass
import os
import requests
from bs4 import BeautifulSoup, PageElement

STATIC_EXTENSIONS = ['.jpg', '.js', '.svg', '.png', '.pdf', '.ttf', '.woff', '.css', '.woff2']


def url_filter(url):
    return 'https://liverpoolmathsschool' in url and '..' not in url

def get_links(soup: BeautifulSoup):
    return set((
        *filter(url_filter, (i.get('href') for i in soup.find_all(href=True))),
        *filter(url_filter, (i.get('src') for i in soup.find_all(src=True)))
    ))

def manipulate_links(soup: BeautifulSoup):
    i: PageElement
    for i in soup.find_all(href=True):
        i['href'] = i['href'].replace('https://liverpoolmathsschool.org', "http://localhost").split('?')[0]
    for i in soup.find_all(src=True):
        i['src'] = i['src'].replace('https://liverpoolmathsschool.org', "http://localhost").split('?')[0]

def save_static(data, path: str):
    path = ''.join(map(lambda x: x if '/' != x else '\\', path))
    folder = '\\'.join(path.split('\\')[:-1])
    print(path)
    os.makedirs(folder, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(data)

def load_page(url):

    return requests.get(url)

def resolve_url(url, path):
    if any(map(lambda x: x in url, STATIC_EXTENSIONS)):
        c, s = resolve_static(url, path)
        save_static(c, s)
        return set()

    else:
        data, path = resolve_static(url, path)
        soup = BeautifulSoup(data.decode())
        links = get_links(soup)
        manipulate_links(soup)
        save_static(soup.prettify().encode(), path)
        return set((i.split('?')[0] for i in links))


def tidy_url(url):
    url = url.split('?')[0]

    if url[-1] == '/':
        url = url + 'index.html'

    if '.' not in url[-6:]:
        url = url + '/index.html'
    return url

def resolve_static(url: str, path: str):
    req = load_page(url)
    url = tidy_url(url)
    subd = url.removeprefix('https://liverpoolmathsschool.org/')
    
    return req.content, path + subd


def main():
    PATH = 'C:\\Users\\richa\\Development\\remote\\liverpoolmathsschool.xyz\\site2\\'
    ROOT = 'https://liverpoolmathsschool.org/'

    urls = resolve_url(ROOT, PATH)
    resolved = set([ROOT])

    while urls:
        url = urls.pop()
        try:
            resolved.add(url)
            print(url, end=' ')
            nurls = resolve_url(url, PATH)
            nurls.difference_update(resolved)
            for i in nurls:
                urls.add(i)
        except KeyboardInterrupt as _:
            break
        except:
            print(f'Url failed: {url}')

if __name__ == '__main__':
    main()
