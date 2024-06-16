# Author: naisu-dev <https://github.com/naisu-dev>
# License: MIT

from setuptools import setup
import braipy

DESCRIPTION = ""
NAME = "braipy"
AUTHOR = "naisu-dev"
AUTHOR_EMAIL = ""
URL = "https://github.com/naisu-dev/braipy"
LICENSE = "MIT"
DOWNLOAD_URL = "https://github.com/naisu-dev/braipy"
VERSION = braipy.__version__

INSTALL_REQUIRES = []

PACKAGES = ["braipy"]

with open("README.md", "r") as f:
  readme = f.read()

setup(description=DESCRIPTION,
     name=Name,
     author=AUTHOR,
     author_email=AUTHOR_EMAIL,
     url=URL,
     license=LICENSE,
     download_url=DOWNLOAD_URL,
     version=VERSION)
