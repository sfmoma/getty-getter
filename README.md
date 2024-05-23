# Getty Getter

A script developed by SFMOMA for associating artists with the Getty ULAN vocabulary and gathering additional metadata based on an artist's ULAN.

The ULAN vocabulary is a wealth of information regarding people and organizations involved in art and culture.  More about ULAN can be found [here](http://www.getty.edu/research/tools/vocabularies/ulan/about.html).

### Usage

This script is a work in progress.  Right now there are four basic functions.


#### 1. get_getty_ulan
`get_getty_ulan` which consumes and artist's name (formatted 	`u'Last, First'`) and does a best guess match against similar names in the Getty ULAN vocabulary.  The returned data will include the name of the artist or organization, the ULAN, the "type" og thing returned (e.g. person, organization etc) and a scope note, which is a brief summary of the artist's career.

`get_getty_ulan(u"Stieglitz, Alfred")`
```
{'scopenote': u'Renowned photographer Stieglitz first studied photochemistry with Hermann Wilhelm Vogel at the Technische Hochschule in Berlin, from 1882-1886, and took his first photographs in 1883. He continued to travel and photograph in Germany, Austria, and Switzerland until 1890, when he returned to New York City. From 1890 to 1895 he was a partner in a photogravure firm. During this time he concentrated on photographing the streets of New York City. In 1894, Stieglitz travelled to Europe and was elected a member of the Linked Ring, a pictorialist society in London. In 1902, Stieglitz founded the Photo-Secession Movement which attempted to prove that pictorialist photography was a fine art form. From 1903 to 1917, Stieglitz was publisher and director of Camera Work magazine. The graphic section was run by Edward Steichen (1879-1973). In 1905, Stieglitz opened the Little Galleries of the Photo-Secession "291" on Fifth Avenue in New York City with Steichen. The galleries operated until 1917. In 1907, Stieglitz exhibited his autochrome photographs. Stieglitz stopped photographing in 1937. During his lifetime, Stieglitz was also a close friend and collaborator of Joseph T. Keiley. Together they invented the glycerine process which permitted partial development of platinum papers. Also, they produced joint research on the history of photography. Keiley also acted as the associate editor of Stieglitz\'\'s publications "Camera Notes" and "Camera Works". American photographer.', 'ulan': u'500024301', 'type': u'Persons, Artists', 'term': u'Stieglitz, Alfred'}
```

#### 2. get_getty_relationship
`get_getty_relationship` which consumes an artist's ULAN and returns a list of the relationships that artist had with other artists in the ULAN vocabulary.  The `object_ulan` being the ULAN of the related person or organization.
`get_getty_relationship("500024301")`
```
{'relationship_type': u'student of', 'object_ulan': u'500063166'}{'relationship_type': u'influenced', 'object_ulan': u'500007426'}{'relationship_type': u'colleague of', 'object_ulan': u'500004441'}{'relationship_type': u'collaborated with', 'object_ulan': u'500001336'}{'relationship_type': u'collaborated with', 'object_ulan': u'500000431'}{'relationship_type': u'spouse of', 'object_ulan': u'500018666'}{'relationship_type': u'friend of', 'object_ulan': u'500070483'}
```

#### 3. get_getty_artist_name
`get_getty_artist_name` which consumes an ULAN and returns just the artist's name formatted `Last, First`.
`get_getty_artist_name("500024301")`
```Stieglitz, Alfred```

#### 4. get_getty_artist_data
`get_getty_artist_data` which consumes an ULAN and returns entire set of data from given ulan as a dictionary.
`get_getty_artist_data("500024301")`
```yaml
{'@context': 'https://linked.art/ns/v1/linked-art.json',
 '_label': 'Stieglitz, Alfred',
 'born': {'id': 'http://vocab.getty.edu/ulan/activity/birth/4000062133',
          'timespan': {'begin_of_the_begin': '1864-01-01T00:00:00',
                       'end_of_the_end': '1864-12-31T23:59:59',
                       'id': 'http://vocab.getty.edu/ulan/time/birth/4000062133',
                       'type': 'TimeSpan'},
          'took_place_at': [{'_label': 'Hoboken',
                             'id': 'http://vocab.getty.edu/tgn/7013711-place',
                             'type': 'Place'}],
          'type': 'Birth'},
...
  ```
The dictionary is parsed from [this json file on ULAN](http://vocab.getty.edu/ulan/500024301.json)

### Installation

`pip install getty-getter`

Getty Getter was built on Django 1.8 and Python 3.12.

### Example View

```python
from django.views.generic.base import View
from django.http import HttpResponse
from getty_getter import getty_getter as getty
import json

class GetUlanView(View):
	def get(self, request):

		artist_ulan = json.dumps(getty.get_getty_ulan(u"Stieglitz, Alfred"))

		return HttpResponse(artist_ulan, content_type="application/json")
```

### Build
For maintainers of this package only.

Download setuptools:
`pip install --upgrade setuptools`

Run this command to build package:
`python -m build`
