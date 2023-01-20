# Python packaging tutorial with an over-simplified downloader

This is an over-simplified downloader package just to
demonstrate python packaging.

It contains a python module to import and a CLI tool.

## Installation

You can easily install the module using `pip`.

## Using the Python module

Once installed, in your python script:

```
from downloader import download

# suppose "url" variable points to a resource to be downloaded.
# "dest_path" variable points to a local path where the resource
# is to be stored.

print(f"Downloading {url} to {dest_path}...")
file_size = downloader(url, dest_path)
print(f"Download successful! File size: {file_size} B")

```

## Using the CLI command

```
$ download <url> -o <dest_path>
```