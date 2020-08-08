import re
import json
import os
from sys import argv, stdout
from requests_html import HTMLSession, HTMLResponse


def makeItem(query, url, title, subtitle):
    icon = "ravenround.gif"
    item = {
        'uid': url,
        'title': title,
        'subtitle': subtitle,
        'arg': url,
        'autocomplete': query,
        'icon': {
            'path': icon
        }
    }
    return item


def makeReturn(items):
    out = {'items': items}
    return out


def get_download_link(url: str) -> str:
    session: HTMLSession = HTMLSession()
    r: HTMLResponse = session.get(f"https://sci-hub.tw/{url}")
    onclick: str = r.html.xpath("//div[@id='buttons']//li/a/@onclick",
                                first=True)
    link: re.Pattern = re.compile(r"'(\S+)'")
    download_url: str = "https:" + link.search(onclick).group(1)
    return download_url


def main():
    arg_c = len(argv)
    if arg_c <= 1:
        return makeReturn([])
    url = argv[1]
    if not url:
        return makeReturn([])
    download_url = get_download_link(url)
    item = [makeItem(url, download_url, "Download link", download_url)]
    out = makeReturn(item)
    return json.dumps(out, indent=4) + '\n'


if __name__ == '__main__':
    download_url = main()
    stdout.write(download_url)
