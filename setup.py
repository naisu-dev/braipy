import re

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('./braipy/__init__.py') as f:
    version = re.findall(r"__version__ = '(.+)'", f.read())[0]

setup(
    name='braipy',
    version=version,
    install_requires=[],
    description='Tenji',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/naisu-dev/braipy',
)
