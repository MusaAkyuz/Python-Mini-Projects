"""
The command-line interface for the downloader
"""
import argparse
from .downloader import download


def main():
    parser = argparse.ArgumentParser(
        description="An over-simplified downloader to demonstrate python packaging."
    )
    parser.add_argument(
        "url", type=str,
        help="The URL of the resource to be downloaded."
    )
    parser.add_argument(
        "--output", "-o",
        help=("Destination local file path. If not set, the resource "
                "will be downloaded to the current working 