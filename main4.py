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
# Titles
* hello Holberton
* Holberton School
* Webstack
# ORderd list
- BUW
- Biblioteka Naradowa
- Biblioteka Politechnica
- DS reviria
"""
with open(fn_md, 'w') as f:
    f.write(c)

# run
os.system("./markdown2html.py {} {}".format(fn_md, fn_html))
time.sleep(1)

li_result = [
    "hello Holberton",
    "Holberton School",
    "Webstack"
]

# parse HTML file
with open(fn_html, "r") as f:
    root = BeautifulSoup(f.read(), 'html.parser')
    all_ol_tags = root.find_all("ol")
    if len(all_ol_tags) == 0:
        print("No tag found")
        exit(1)
    if len(all_ol_tags) != 1:
        print("Too many tags: {}".format(all_ol_tags))
        exit(1)
    ol_tag = all_ol_tags[0]
    for ol_tag_child in ol_tag.children:
        if ol_tag_child.name is None:
            continue
        if ol_tag_child.name != 'li':
            print("Wrong tag name: {}".format(ol_tag_child.name))
            exit(1)
        li_content = ol_tag_child.string.strip()
        if li_result[0] != li_content:
            print("Wong value: {} instead of {}".format(li_content, li_result[idx]))
            exit(1)
        del li_result[0]

    if len(li_result) != 0:
        print("Some LI are not found: {}".format(li_result))
        exit(1)

    print("OK", end="")

