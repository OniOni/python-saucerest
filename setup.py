import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-saucerest",
    packages = ['saucelabs'],
    version = "0.0.2",
    author = "Mathieu Sabourin",
    author_email = "mathieu.c.sabourin@gmail.com",
    maintainer = "Mathieu Sabourin",
    maintainer_email = "mathieu.c.sabourin@gmail.com",
    description = ("Python wrapper around the saucelabs REST API"),
    keywords = " Sauce Labs, REST",
    url = "https://github.com/OniOni",
    download_url = "https://github.com/OniOni/python-saucerest",
    install_requires = ["selenium>=2.21.3"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        ]
)
