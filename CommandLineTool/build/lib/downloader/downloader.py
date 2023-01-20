import requests

def download(url, dest_path=None):
    res = requests.get(url)
    res.raise_for_status()
    if dest_path is None: # grab the url basename
        dest_path = url.split("/")[-1]
    with open(dest_path, 'wb') as fhand:
        return fhand.write(res.content)