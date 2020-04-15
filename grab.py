import os
import json
import sys
import urllib.request
import urllib.parse

from lxml import etree


link, download_folder = sys.argv[1:]
os.makedirs(download_folder, exist_ok=True)
_, hash = os.path.split(urllib.parse.urlparse(link).path)
data = urllib.request.urlopen(link)
tree = etree.parse(data, etree.HTMLParser())
el, = tree.xpath("//script[@id='coubPageCoubJson']")
url = json.loads(el.text)['file_versions']['share']['default']
video, _ = urllib.request.urlretrieve(url)
os.rename(video, os.path.join(download_folder, f'{hash}.mp4'))
