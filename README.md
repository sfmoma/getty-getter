# getty_scraper

A script developed by SFMOMA for associating artists with the Getty ULAN vocabulary and gathering additional metadata based on an artist's ULAN.

The ULAN vocabulary is a wealth of information regarding people and organizations involved in art and culture.  More about ULAN can be found [here](http://www.getty.edu/research/tools/vocabularies/ulan/about.html).

This script is a work in progress.  Right now there are three basic functions.

1. `get_getty_ulan` which consumes and artist's name (formatted u`First, Last`) and does a best guess match against similar names in the Getty ULAN vocabulary.
2. `get_getty_relationship` which consumes an artist's ULAN and returns a list of the relationships that artist had with other artists in the ULAN vocabulary.
3. `get_getty_artist_name` which consumes an ULAN and returns just the artist's name formatted `First Last`.
