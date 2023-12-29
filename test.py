#!/usr/bin/python3


from bs4 import BeautifulSoup
from sys import argv
# parse HTML file
file = argv[1]
with open(file, "r") as f:
    root = BeautifulSoup(f.read(), 'html.parser')
    all_tag_names = [tag.name for tag in root.find_all()]
    if len(all_tag_names) == 0:
        print("No tag found")
        exit(1)
    if len(all_tag_names) != 1:
        print("Too many tags: {}".format(all_tag_names))
    if all_tag_names[0] != 'h2':
        print("H2 not found: {}".format(all_tag_names[0]))
    print("OK", end="")