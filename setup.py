#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re
import sys

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


package = 'tapioca_qualys_was'
requirements = [
    'tapioca-wrapper<2',

]
test_requirements = [

]

def _exec(cmd):
    try:
        stdout = subprocess.check_output(cmd, shell=True,
                                         universal_newlines=True)
    except subprocess.CalledProcessError as e:
        stdout = e.output
    lines = stdout.splitlines()
    return [line.rstrip() for line in lines if line.rstrip()]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    head_sha = _exec("git rev-list -n 1 HEAD")[0]
    count_sice = _exec("git rev-list --count HEAD \"^{head_sha}\"".format(head_sha=head_sha))
    version = re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)

    return version + '.' + str(count_sice[0])


def get_author(package):
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


def get_email(package):
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


# python setup.py register
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name='tapioca-qualys_was',
    version=get_version(package),
    description='qualys_was API wrapper using tapioca',
    long_description=readme,
    author=get_author(package),
    author_email=get_email(package),
    url='https://github.com/siteblindado/tapioca-qualys_was',
    packages=[
        'tapioca_qualys_was',
    ],
    package_dir={'tapioca_qualys_was': 'tapioca_qualys_was'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='qualys_was',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
