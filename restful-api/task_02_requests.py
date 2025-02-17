#!/usr/bin/python3
"""
At the end of this exercise, students should be able to:
Utilize the requests library to send HTTP requests and process responses.
Parse and manipulate JSON data using Python.
Convert structured data into other formats, e.g., CSV.
"""
import requests
import csv


def fetch_and_print_posts():
    """
     function fetch_and_print_posts()
     """
     response = requests.get('https://jsonplaceholder.typicode.com/posts')
     print(f"Status Code: {response.status_code}")
     if response.status_code == 200:
         posts = response.json()
         for post in posts:
             print(post["title"])

def fetch_and_save_posts():
    """
    function fetch_and_save_posts()
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
         posts = response.json()
         data = [{'id': post['id'], 'title': post['title'],
                'body': post['body']} for post in posts]

         with open("posts.csv", "w") as c:
             writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
             writer.writeheader()
             writer.writerows(structured_data)
