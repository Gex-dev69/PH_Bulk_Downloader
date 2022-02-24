from pornhub import PornHub
from pySmartDL import *
from scapper import scrappy


keywords = ["milf","latina"]
client = PornHub(keywords)


def main():
    for video in client.getVideos(50,page=1):
        scrappy(video["url"])


main()