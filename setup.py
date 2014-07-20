from distutils.core import setup
from setuptools import find_packages

version='0.0.1'

setup(
    name='urban_dictionary_words',
    long_description='Urban Dictionary Word Downloader',
    author='Hatem Nassrat',
    zip_safe=False,
    version=version,
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
        'scrapy',
        'service_identity', # optional
    ],
    entry_points={
    },
)
