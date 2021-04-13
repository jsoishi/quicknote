#!/usr/bin/env python3

import jinja2 
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", metavar='filename', type=str, help="name of the file.")
    parser.add_argument("-d", "--doctype", dest='doctype', help = "Type of note. Options are teaching, research.", default="teaching")
    parser.add_argument("-t", "--title", dest='title', help = "Title of note", default='Title')
    parser.add_argument("-c", "--class", dest='classname', help = "For teaching, course number.", default="Bates PHYS")

    args = parser.parse_args()
    latex_jinja_env = jinja2.Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader = jinja2.PackageLoader('quicknote', 'templates')
    )
    filename = args.filename
    if not filename.endswith('.tex'):
        filename += '.tex'

    if args.doctype == "research":
        print("research")
        template = latex_jinja_env.get_template("research.tex")
    else:
        print("teaching.")
        template = latex_jinja_env.get_template("teaching.tex")

    out_text = template.render(title=args.title,classname=args.classname)
    with open(filename,'w') as outfile:
        outfile.write(out_text)
