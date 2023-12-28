#!/usr/bin/python3
"""
Markdown2html.py
"""


from sys import argv, stderr
from os import path

args = argv
if len(args) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=stderr)
    exit(1)
elif len(args) == 3:
    if not path.isfile(args[1]):
        print("Missing {}".format(args[1]), file=stderr)
        exit(1)
    elif not path.isfile(args[2]):
        print("Missing {}".format(args[2]), file=stderr)
        exit(1)
    exit(0)
