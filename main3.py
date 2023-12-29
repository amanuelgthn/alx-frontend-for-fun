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

- hello Holberton
- Holberton School
- Webstack

## sub title

- super
- cool
"""
with open(fn_md, 'w') as f:
    f.write(c)

# run
os.system("./markdown2html.py {} {}".format(fn_md, fn_html))
time.sleep(1)

result = [
    { 'name': 'h1', 'value': "title" },
    { 'name': 'ul', 'children': [
        { 'name': 'li', 'value': "hello Holberton" },
        { 'name': 'li', 'value': "Holberton School" },
        { 'name': 'li', 'value': "Webstack" }
    ] },
    { 'name': 'h2', 'value': "sub title" },
    { 'name': 'ul', 'children': [
        { 'name': 'li', 'value': "super" },
        { 'name': 'li', 'value': "cool" }
    ] }
]

# parse HTML file
with open(fn_html, "r") as f:
    root = BeautifulSoup(f.read(), 'html.parser')
    all_tags = root.find_all(recursive=False)
    if len(all_tags) == 0:
        print("No tag found")
        exit(1)
    if len(all_tags) != len(result):
        print("Too many tags: {}".format(all_tags))
        exit(1)
    
    for tag in all_tags:
        r_tag = result[0]
        if tag.name != r_tag['name']:
            print("Wrong name: {} instead of {}".format(tag.name, r_tag['name']))
            exit(1)
        r_tag_children = r_tag.get('children')
        if r_tag_children is not None:
            for tag_child in tag.children:
                if tag_child.name is None:
                    continue
                r_tag_child = r_tag_children[0]
                if tag_child.name != r_tag_child['name']:
                    print("Wrong name: {} instead of {}".format(tag_child.name, r_tag_child['name']))
                    exit(1)
                s_tag_child = tag_child.string.strip()
                if s_tag_child != r_tag_child['value']:
                    print("Wrong content: {} instead of {}".format(s_tag_child, r_tag_child['value']))
                    exit(1)
                del r_tag_children[0]

            if len(r_tag_children) != 0:
                print("Some children tags are not found: {}".format(r_tag_children))
                exit(1)
        else:
            s_tag = tag.string.strip()
            if s_tag != r_tag['value']:
                print("Wrong content: {} instead of {}".format(s_tag, r_tag['value']))
                exit(1)

        del result[0]
    
    if len(result) != 0:
        print("Some tags are not found: {}".format(result))
        exit(1)

    print("OK", end="")

