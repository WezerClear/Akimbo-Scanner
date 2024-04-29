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
        "-s",
        "--speed",
        required=False,
        type=int,
        default=1,
        help="Choose the speed of the scan 1 to 5, default 1",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        required=False,
        help="Active verbose",
    )

    args = parser.parse_args()
    if args.speed > 5 or args.speed < 1:
        return print("Error: speed value should be between 1 and 5")
    subdomainsScan(args.url, args.speed)


def subdomainsScan(url: str, speed: int):
    validSub = []
    sub_list = open("sub.txt").read()
    subdoms = sub_list.splitlines()
    for sub in subdoms:
        sub_domains = f"https://{sub}.{url}"
        try:
            requests.get(sub_domains)

        except requests.ConnectionError:
            pass

        else:
            validSub.append(sub)
    return choiceDir(validSub, url)


def choiceDir(subList: list, url: str):
    index = 0
    choice = ""
    for sub in subList:
        index += 1
        print(index, "-", sub)
    while choice != "end":
        choice = input("Enter sub's name to delete, 'end' to validate\n")
        try:
            subList.remove(choice)
        except:
            if choice != "end":
                print("Enter a valid input\n")
    return directoryScan(subList, url)


def directoryScan(subList: list, url: str):
    pageDict = dict()
    subList.insert(0, "")
    dirList = open("dir.txt").read()
    directories = dirList.splitlines()
    for dir in directories:
        for sub in subList:
            if sub != "":
                dir_enum = f"https://{sub}.{url}/{dir}"
            if sub == "":
                dir_enum = f"https://{url}/{dir}"
            r = requests.get(dir_enum)
            if r.status_code != 404:
                pageDict[dir_enum] = r.status_code
    return print(pageDict)


if __name__ == "__main__":
    main()
