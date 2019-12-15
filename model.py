import urllib.request
import requests
import urllib.parse
from io import BytesIO
import json


# A new class model is created
class Opensourcemodel:

    # initializes the class
    def __init__(self):
        pass

    # gets the name and accesses the ISBN number
    def sub_url_open(self, data):
        base_url = 'http://openlibrary.org/search.json?title='
        sub_url = base_url + data
        response = urllib.request.urlopen(sub_url)
        info = json.load(response)
        isbn_num = info["docs"][0]["isbn"][0]
        return isbn_num

    # gets the ISBN number and access the book cover
    def url_open(self, isbn_num):
        BASEurl = 'http://covers.openlibrary.org/b/isbn/'
        url = BASEurl + isbn_num + '-L.jpg'
        # download image
        with open('picture.jpg', 'wb') as handle:
            resp = requests.get(url, stream=True)

            if not resp.ok:
                print(resp)

            for block in resp.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        x = urllib.request.urlopen(url)
        cover = x.read()
        cover = BytesIO(cover)
        return cover
