#!/usr/bin/python3
"""
Markdown2html.py
"""


from sys import argv, stderr
from os import path


def parse_markdown(filemd, filehtml):
    """Read and parse a Markdown file"""
    HTML_generated = {}
    list_generated = []
    count = 0
    count_ul = 0
    count_ol = 0
    title = ''
    with open(filemd, 'r') as file:
        for line in file.readlines():
            if line.startswith('#'):
                list = line.split(' ')
                count += 1
                with open(filehtml, 'a') as file:
                    if count_ul != 0:
                        file.write("</ul>\n")
                    if count_ol != 0:
                        file.write("</ol>\n")
                    title = ' '.join(list[1:])
                    script = "<h{}>{}</h{}>".format(len(list[0]),
                                                    title.rstrip('\n'),
                                                    len(list[0]))
                    file.write("{}\n".format(script))
                    count_ul = 0
                    count_ol = 0
            if line.startswith('-'):
                count_ol = 0
                ul = line.split(' ')
                ul = ' '.join(ul[1:])
                with open(filehtml, 'a') as file:
                    if count_ul == 0:
                        file.write("{}\n".format("<ul>"))
                    file.write("\t<li>{}</li>\n".format(ul.rstrip('\n')))
                    count_ul += 1
            if line.startswith('*'):
                count_ul = 0
                ol = line.split(' ')
                ol = ' '.join(ol[1:])
                with open(filehtml, 'a') as file:
                    if count_ol == 0:
                        file.write("{}\n".format("<ol>"))
                    file.write("\t<li>{}</li>\n".format(ol.rstrip('\n')))
                    count_ol += 1

    # Add </ul> tag after processing all lines
    with open(filehtml, 'a') as file:
        if count_ul != 0:
            file.write("</ul>\n")
    # Add </ol> tag after processing all lines
    with open(filehtml, 'a') as file:
        if count_ol != 0:
            file.write("</ol>\n")


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
