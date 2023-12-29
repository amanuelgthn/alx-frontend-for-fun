#!/usr/bin/python3
"""
Test case
"""
import os
import random
import string
import time
from bs4 import BeautifulSoup

def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


fn_md = "{}.md".format(random_string())
fn_html = "{}.html".format(random_string())

# remove initial MD file
if os.path.exists(fn_md):
    os.remove(fn_md)

# remove initial HTML file
if os.path.exists(fn_html):
    os.remove(fn_html)

# create MD file
c = """
# title
"""
with open(fn_md, 'w') as f:
    f.write(c)

# run
os.system("./markdown2html.py {} {}".format(fn_md, fn_html))
time.sleep(1)

# parse HTML file
with open(fn_html, "r") as f:
    root = BeautifulSoup(f.read(), 'html.parser')
    all_tag_names = [tag.name for tag in root.find_all()]
    if len(all_tag_names) == 0:
        print("No tag found")
        exit(1)
    if len(all_tag_names) != 1:
        print("Too many tags: {}".format(all_tag_names))
    if all_tag_names[0] != 'h1':
        print("H1 not found: {}".format(all_tag_names[0]))
    print("OK", end="")

# delete files
""" if os.path.exists(fn_md):
    os.remove(fn_md)
if os.path.exists(fn_html):
    os.remove(fn_html) """