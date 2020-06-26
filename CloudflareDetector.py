# (c) HanzHxaors 2020

import requests
import sys
import socket


def detect(protocol, url):
    res = requests.get(protocol+url, verify=False, headers={"X-Powered-By":"HaznHaxors"})
   
    if len(sys.argv) > 2 and sys.argv[2] == "-v":
        print(res.text)

    if "direct ip access not allowed" in res.text.lower():
        print("[!] Website protected by CloudFlare.")
        exit()
    else:
        print("[$] Website not protected by CloudFlare.")
        exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 CloudflareDetector.py [protocol://][URL]")
        exit()

    if len(sys.argv) > 2 and sys.argv[2] == "-v":
        print(sys.argv[1].split("://")[1])

    ip = socket.gethostbyname(sys.argv[1].split("://")[1])
    protocol = sys.argv[1].split("://")[0]+"://"
    detect(protocol, ip)
