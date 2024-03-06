# Copyright (c) 2024, Test and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class TestGit(Document):
	pass


import requests

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def main():
    url = "https://example.com/data"
    data = fetch_data(url)
    print(data)

if __name__ == "__main__":
    main()
