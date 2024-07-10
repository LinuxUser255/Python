#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# Same script as the one for downloading .mp4, with a few changes.
# Enter the complete URL path containg the .pdf files you wish to download.
book_url = " "

def get_pdf_links():
    r = requests.get(book_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')
    # Keep it Simple and just find the files ending in .pdf
    pdf_links = [book_url + link['href'] for link in links if link['href'].endswith('pdf')]

    return pdf_links

def download_all_pdfs(pdf_links):
    for link in pdf_links:
        file_name = link.split('/')[-1]
        print("Downloading file:%s" % file_name)

        # create a request object
        r = requests.get(link, stream=True)

        # download started. Writing the file in binary.
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s has been downloaded\n" % file_name)

    print("pdf downloads complete.")
    return


if __name__=="__main__":
    pdf_links = get_pdf_links()
    download_all_pdfs(pdf_links)
