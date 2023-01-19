import downloader


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    downloader.download("https://www.python.org/static/img/python-logo.png", destination="python_logo1")

