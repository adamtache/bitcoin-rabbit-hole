#! /usr/bin/python3
import gspread
import json
import re

from oauth2client.service_account import ServiceAccountCredentials
from util import author_to_file_path, get_excerpt_from_page, get_valid_author_slug, title_to_file_path

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Copy of Bitcoin Resources").sheet1

for row in sheet.get_all_values():
    if row[0] == '':
        continue

    resource_categories = row[0].split(',')
    resource_type = row[1].lower()
    resource_title_raw = row[2].title()
    resource_title = resource_title_raw.replace(":", "&#58")
    resource_authors = row[3].split(',')
    resource_url = row[4]
    resource_date = row[5]
    resource_excerpt = get_excerpt_from_page(resource_url)

    for author in resource_authors:
        author_slug = get_valid_author_slug(author)

        author_file = (
            f"---\n"
            f"name: {author.strip()}\n"
            f"slug: {author_slug}\n"
            f"permalink: /author/{author_slug}\n"
            f"---")

        author_file_path = author_to_file_path(author_slug)
        with open(author_file_path, 'w') as f:
            f.write(author_file)

    md_file = (
                f"---\n"
                f"layout: {resource_type}\n"
                f"title: {resource_title}\n"
                f"date: {resource_date}\n"
                f"categories: {resource_categories}\n"
                f"author: {resource_authors}\n"
                f"excerpt: {resource_excerpt}\n"
                f"external_url: {resource_url}\n"
                f"---")

    md_file_path = title_to_file_path(resource_title_raw, resource_type)
    with open(md_file_path, 'w') as f:
        f.write(md_file)
