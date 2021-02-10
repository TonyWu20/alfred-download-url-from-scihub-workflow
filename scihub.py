"""
Retrieve pdf download url
"""
import re
import json
from sys import argv, stdout
from requests_html import HTMLSession, HTMLResponse


def makeItem(query: str, url: str, title: str, subtitle: str) -> dict:
    """Format item output for alfred
    """
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


def makeReturn(items: dict) -> dict:
    """
    Format output for alfred
    """
    out = {'items': items}
    return out


def get_download_link(url: str) -> str:
    """Return link
    Args:
        url (str): passed url
    Return:
        url string
    """
    session: HTMLSession = HTMLSession()
    header = "https://"
    if not header in url:
        url = f"{header}{url}"
    scihub_suf = "se"
    r: HTMLResponse = session.get(f"https://sci-hub.{scihub_suf}/{url}")
    onclick: str = r.html.xpath("//div[@id='buttons']//li/a/@onclick",
                                first=True)
    link: str = re.search(r"'(\S+)'", onclick).group(1)
    if not header in link:
        return_url: str = "https:" + link
    else:
        return_url = link
    return return_url


def main():
    """Main function for workflow
    """
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
