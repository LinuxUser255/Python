#!/usr/bin/env python3

"""
Synopsis:

    python3 requests.py

Description:

    Using Object-Oriented Programming (OOP) and guarding.
    This program makes get requests to a url, uses try-except-finally to handle exceptions,
    conditional if-elif to check the status of the request, write the response to a JSON file
    and prints the response code and headers to the console.
"""

import requests
import json

url = "https://api.github.com/"


class OORequests:
    def __init__(self, url):
        """

        :type url: str
        """
        self.url = url
        self.response = None
        self.status_code = None
        self.headers = None
        self.content = None

    # This Method makes requests, handles responses using the try-except-finally block
    def make_request(self):
        try:
            self.response = requests.get(self.url)
            self.status_code = self.response.status_code
            self.headers = self.response.headers
            self.content = self.response.content
        except requests.exceptions.RequestException as e:
            print(e)
            self.response = None
            self.status_code = None
            self.headers = None
            self.content = None
            return False
        return True

    # This  Method  writes the response to a JSON file in dictionary format
    def write_to_json(self):
        with open("response.json", "w") as f:
            f.write(json.dumps(self.response.json(), indent=4))
        return True

    # Main function
    def main(self):
        if self.make_request():
            if self.write_to_json():
                print(f"Status Code: {self.status_code}")
                print(f"Headers: {self.headers}")
                print(f"Content: {self.content}")
            else:
                print("Error writing to JSON file")
        else:
            print("Error making request")


# call the main function
if __name__ == "__main__":
    oor = OORequests(url)
    oor.main()
