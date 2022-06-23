import os, sys, csv, requests, time
import  urllib
import requests
from urllib import response
from urllib.request import Request
import urllib.parse
import ssl


def check_url(url):
    try:

        requests = Request("http://" + url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' })
        contents = urllib.request.urlopen(requests)
        code = contents.getcode()
        print("http://" +  url + " " + str(code) + " Size:" + str(sys.getsizeof(contents.read())) + "B" )

        contents.close()

    except urllib.error.HTTPError as http_err:
        print("http://" + url + " " + str(http_err))
    except urllib.error.URLError as url_err:
        print("http://" + url + " " + str(url_err))
    except :
        print("http://" + url + " " + str(sys.exc_info()[0]))



    try:

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        requestss = Request("https://" + url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        contentss = urllib.request.urlopen(requestss, context=ctx)
        codes = contentss.getcode()
        print("https://" + url + " " + str(codes) + " Size:" + str(sys.getsizeof(contentss.read())) + "B")
        contents.close()
    except urllib.error.HTTPError as http_err:
        print("https://" + url + " " + str(http_err))
    except urllib.error.URLError as url_err:
        print("https://" + url + " " + str(url_err))
    except :
        print("https://" + url + " " + str(sys.exc_info()[0]) )








with open("url_dataset.csv", "r") as f:
    for line in f:

        test_line = line.split(";")
       # print(test_line)
        iter_line = iter(test_line)
        next(iter_line)
        print("========= " + test_line[0] + " =========")
        for x in iter_line:
            if len(x) > 2:
                #print(x)
                check_url(x)

        print(" ")


