#!/usr/bin/env python

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    if '{{ cookiecutter.create_repoman_travis_cfg }}' != 'y':
        remove_file('.travis.yml')

    if '{{ cookiecutter.create_readme }}' != 'y':
        remove_file('README.md')
