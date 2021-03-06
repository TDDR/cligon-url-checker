#!/usr/bin/env python3
"""
C.L.I.G.O.N
Check if Link Is Good Or Not
Written in Python 3.8.2
"""

import sys
import argparse
from src.url_checker import UrlChecker

VERSION = 0.1


def main():
    """cligon main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", help="input file to check URL links")
    parser.add_argument(
        "-v",
        "--version",
        help="display program name and version number",
        action="version",
        version="C.L.I.G.O.N (Check if Link Is Good Or Not) - CLIGON - " + str(VERSION),
    )
    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="output program results into JSON format",
    )
    parser.add_argument(
        "--all", action="store_true", help="default, output all url types"
    )
    parser.add_argument("--good", action="store_true", help="only display good urls")
    parser.add_argument("--bad", action="store_true", help="only display bad urls")
    args = parser.parse_args()
    if args.filename:
        try:
            time_out = 2.5
            checker = UrlChecker()
            urls = checker.parse_urls_from_file(args.filename)
            urls_status_list = checker.check_urls_thread(urls, time_out)
            checker.output_urls_and_status(urls_status_list, args)
            del urls_status_list
        except FileNotFoundError:
            print("error: inputted file not found")
    else:
        parser.print_help()

    return sys.exit(0)


if __name__ == "__main__":
    main()
