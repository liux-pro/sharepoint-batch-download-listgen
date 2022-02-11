import os
import time
from pyaria2 import Aria2RPC
#  pyaria2=0.1.1

def get_file_from_url(link, file_name):
    jsonrpc = Aria2RPC("http://1.1.1.11:6800/rpc", "xxxxxx")

    options = {"dir": "/downloads/hors", "out": file_name, "header": [
        'Cookie: FedAuth=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']}
    res = jsonrpc.addUri([link], options=options)


list = []

if __name__ == '__main__':
    count = 0
    for i in list:
        count = count + 1
        get_file_from_url(i, "{}.mp4".format(count))
