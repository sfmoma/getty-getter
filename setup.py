
import setuptools

VERSION = 0.1

setuptools.setup(name='Getty Getter',
      version=VERSION,
      description='Getty ULAN scraping utilities',
      author='Jay Mollica',
      author_email='jmollica@sfmoma.org',
      url='https://github.com/jaymollica/getty_scraper',
      packages=['getty_scraper'],
      scripts=['getty_scraper.py'],
      keywords='Getty Art ULAN SFMOMA Artist Artwork',
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "License :: Free for non-commercial use",
        "Programming Language :: Python :: 2.7",
        ],
      install_requires=[
        'pycurl',
        'python-Levenshtein',
        ],
     )