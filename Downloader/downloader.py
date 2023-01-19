import requests


def download(url, destination=None):
    res = requests.get(url)
    res.raise_for_status()

    if destination is None:
        destination = url.split("/")[-1]
    with open(destination, "wb") as file:
        return file.write(res.content)