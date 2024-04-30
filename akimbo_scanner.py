import requests
import sys
import argparse
import time


def main():

    print(
        '''                                   
  +-'~`---------------------------------/\--
 ||"""""""""""""""""""""""""""""""" \\\\\\  \/~)
 ||    AUTHOR SGB                    \\\\\\  \/_
  |~~~~~~~~-________________-_________________\ ~--_
  !---------|_________       ------~~~~~(--   )--~~
                      \ /~~~~\~~\   )--- \_ /(
                       ||     |  | \   ()   \\
                       \\____/_ / ()\        \\
                        `~~~~~~~~~-. \        \\
                                    \ \  <($)> \\
                                     \ \        \\
                                      \ \        \\
      AKIMBO__                         \ \        \\
         SCANNER__                      \ \  ()    \|
                                        _\_\__====~~~               
\n
'''
    )

    parser = argparse.ArgumentParser(
        prog="Akimbo Scanner",
        description="Scanner for Subdomains and Directory",
        epilog="dev: WezerClear / SGB  GitHub: https://github.com/WezerClear",
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
    taille = len(subdoms)
    progress_step = max(taille // 30, 1)
    for i, sub in enumerate(subdoms):
        sub_domains = f"https://{sub}.{url}"
        try:
            requests.get(sub_domains)

        except requests.ConnectionError:
            pass

        else:
            validSub.append(sub)
        if (i + 1) % progress_step == 0 or i == taille - 1:
            progress = min((i + 1) / taille * 100, 100)
            done = int(progress / (100 / 30))
            remaining = 30 - done
            print(f"{i+1}/{taille}", "#" * done + "." * remaining, end="\r")
    return choiceDir(validSub, url)


def choiceDir(subList: list, url: str):
    index = 0
    choice = ""
    print("\n")
    for sub in subList:
        index += 1
        print(index, "-", sub)
    print("\n")
    while choice != "end":
        choice = input("Enter sub's name to delete, 'end' to validate\n")
        try:
            subList.remove(choice)
        except:
            if choice != "end":
                print("Enter a valid input\n")
    print("\n\n")
    print(
        f"""
   __________________                         ________
   | Akimbo Scanner |                         | v1.0 |
-------------------------------------------------------------
| target's url         |  {url}
|----------------------|-------------------------------------
| target's subdomains  |  {subList}                                  
|------------------------------------------------------------
|      author: SGB     |  https://github.com/WezerClear       
-------------------------------------------------------------
"""
    )
    return directoryScan(subList, url)


def directoryScan(subList: list, url: str):
    pageDict = dict()
    subList.insert(0, "")
    dirList = open("dir.txt").read()
    directories = dirList.splitlines()
    taille = len(directories) * len(subList)
    progress_step = max(taille // 30, 1)
    i = 0
    for dir in directories:
        for sub in subList:
            if (i + 1) % progress_step == 0 or i == taille - 1:
                progress = min((i + 1) / taille * 100, 100)
                done = int(progress / (100 / 30))
                remaining = 30 - done
                print(f"{i+1}/{taille}", "#" * done + "." * remaining, end="\r")
            i += 1
            if sub != "":
                dir_enum = f"https://{sub}.{url}/{dir}"
            if sub == "":
                dir_enum = f"https://{url}/{dir}"
            r = requests.get(dir_enum)
            if r.status_code != 404:
                pageDict[dir_enum] = r.status_code

    return display(subList, url, pageDict)


def display(subList: list, url: str, pageDict: dict):
    displaySub = ""
    subList.pop(0)
    for sub in subList:
        displaySub += sub + " "
    print(f"\nResult for [{url}] with {displaySub}\n")
    for result in pageDict:
        print(f"{result} -> [{pageDict[result]}]")
    print("\n")


if __name__ == "__main__":
    main()
