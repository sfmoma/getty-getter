
import setuptools

VERSION = "0.2"

setuptools.setup(name='getty-getter',
      version=VERSION,
      description='Getty ULAN scraping utilities',
      author='Jay Mollica, Fangyi Zhu',
      author_email='jmollica@sfmoma.org',
      url='https://github.com/sfmoma/getty-getter',
      packages=['getty_getter'],
      keywords='SFMOMA Getty Art ULAN Artist Artwork Museums',
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