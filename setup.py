
import setuptools

VERSION = "0.2"

setuptools.setup(name='artist_getter',
      version=VERSION,
      description='Getty ULAN and WikiData scraping utilities for artists',
      author='Jay Mollica, Fangyi Zhu',
      url='https://github.com/fangyizhu/artist-getter',
      packages=['artist_getter'],
      keywords='Getty Art ULAN WikiData Artist Artwork Museums',
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "License :: Free for non-commercial use",
        "Programming Language :: Python :: 3.12",
        ],
      install_requires=[
        'pycurl',
        'python-Levenshtein',
        ],
     )