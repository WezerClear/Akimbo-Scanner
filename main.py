import requests
import sys
import argparse
import time


def main():

    parser = argparse.ArgumentParser(
        prog="sub-dir",
        description="sub-dir",
        epilog="dev: WezerClear / SGB  GitHub: https://github.com/WezerClear ",
    )

    parser.add_argument("-u", "--url", required=True, type=str, help="Target's url")

    parser.add_argument(
        "-S",
        "--Subdomain",
        required=False,
        type=str,
        help="Wordlist for Subdomains",
    )
    parser.add_argument(
        "-D",
        "--Directory",
        required=False,
        type=str,
        help="Wordlist for directory",
    )

    parser.add_argument(
        "-s",
        "--subdomain",
        required=False,
        type=str,
        help="Select your words for Subdomains",
    )
    parser.add_argument(
        "-d",
        "--directory",
        required=True,
        type=str,
        help="Select your words for directory",
    )

    parser.add_argument(
        "--speed",
        action="store_true",
        required=False,
        help="Choose the speed of the scan 1 to 5",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        required=False,
        help="Active verbose",
    )

    args = parser.parse_args()


sub_list = open("subdomains.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_domains)


sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code == 404:
        pass
    else:
        print("Valid directory:", dir_enum)
