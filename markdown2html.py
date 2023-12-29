#!/usr/bin/python3
"""
Markdown2html.py
"""


from sys import argv, stderr
from os import path


def parse_markdown(filemd, filehtml):
    """Read and parse a Markdown file"""
    HTML_generated = {}
    count = 0
    title = ''
    with open(filemd, 'r') as file:
        for line in file.readlines():
            if line.startswith('#'):
                list = line.split(' ')
                HTML_generated[count] = list
                count += 1
    with open(filehtml, 'a') as file:
        for i in range(count):
            title = ' '.join(HTML_generated[i][1:])
            script = "<h{}>{}</h{}>".format(len(HTML_generated[i][0]),
                                            title.rstrip('\n'),
                                            len(HTML_generated[i][0]))
            file.write("{}\n".format(script))


if __name__ == '__main__':
    """Taking and checking arguments"""
    args = argv
    if len(args) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    elif len(args) == 3:
        if not path.isfile(args[1]):
            print("Missing {}".format(args[1]), file=stderr)
            exit(1)
    parse_markdown(args[1], args[2])
    exit(0)
