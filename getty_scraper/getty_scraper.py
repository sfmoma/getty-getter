import requests
import urllib
import json
import pycurl
from Levenshtein import distance
from StringIO import StringIO

# returns entire set of data from given ulan
def get_getty_artist_data(ulan):
	return

# returns artist name from given ulan
def get_getty_artist_name(ulan):
	url = "http://vocab.getty.edu/ulan/%s.json" % ulan
	result = requests.get(url)
	data = json.loads(result.content)
	
	bindings = data['results']['bindings']

	for binding in bindings:
		if binding['Object']['type'] == 'literal':
			getty_artist_name = binding['Object']['value']
			break
			
	return getty_artist_name

# returns a list of ulans and their relationship to the provided ulan
def get_getty_relationship(ulan):
	url = "http://vocab.getty.edu/ulan/%s.json" % ulan
	result = requests.get(url)
	relationships = list()
	data = json.loads(result.content)

	bindings = data['results']['bindings']

	for binding in bindings:
		
		predicate_url = binding['Predicate']['value']
		object_url = False

		# relationships are determined if the linked content has an ulan
		if "#ulan" in predicate_url:
			p_url_parts = predicate_url.split("#")
			predicate = p_url_parts[1]
			object_url = binding['Object']['value']

		if (object_url):
			o_url_parts = object_url.split("/ulan/")
			object_ulan = o_url_parts[1]

			predicate_parts = predicate.split("_")
			predicate_parts.pop(0)
			relationship_display = " ".join(predicate_parts)

			relationship = {'relationship_type':relationship_display, 'object_ulan': object_ulan}
			relationships.append(relationship)

	return relationships

# returns a best guess ulan based on artist's name (formatted: Lastname, Firstname) and some basic info
def get_getty_ulan(artist):
	# artists with apostrophies in their names need escaping
	if(artist.find("'") != -1 ):
		artist = artist.replace("'","\\\'")

	# get rid of any whitespace and encode to utf8
	artist = artist.replace('\n', ' ').replace('\r', '')
	artist_encoded = urllib.quote(artist.encode('utf8'));

	# sparql query that could use some refining
	getty_url = 'http://vocab.getty.edu/sparql.json?query=select+%3FSubject+%3FTerm+%3FParents+%3FScopeNote+%7B%0D%0A++%3FSubject+a+skos%3AConcept%3B+luc%3Aterm+%27+%22'+artist_encoded+'%22+%27%3B%0D%0A+++++gvp%3AprefLabelGVP+%5Bxl%3AliteralForm+%3FTerm%5D.%0D%0A++optional+%7B%3FSubject+gvp%3AparentStringAbbrev+%3FParents%7D%0D%0A++optional+%7B%3FSubject+skos%3AscopeNote+%5Bdct%3Alanguage+gvp_lang%3Aen%3B+rdf%3Avalue+%3FScopeNote%5D%7D%7D&_implicit=false&implicit=true&_equivalent=false&_form=%2Fsparql'

	# curl is required due to requests package tripping on some character strings
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, getty_url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	result = buffer.getvalue()
	data = json.loads(result)
	bindings = data['results']['bindings']

	ulans = list()
	if (bindings):
		for b in bindings:
			b_subject = b['Subject']['type']
			if (b_subject == 'uri'):
				b_uri = b['Subject']['value']
				uri_parts = b_uri.split('/ulan/')
				if(len(uri_parts) == 2):
					ulan = uri_parts[1]
				else:
					# these URIs tend to lead to other vocabularies (TGN, AAT etc)
					continue

			b_type = b['Parents']['value']
			b_term = b['Term']['value']

			#prepare apostrophies for insertion into psql db, TO DO: move this to the view logic
			b_term = b_term.replace("'","''")

			if('ScopeNote' in b):
				b_scopenote = b['ScopeNote']['value']
				b_scopenote = b_scopenote.replace("'","''")
			else:
				b_scopenote = None

			getty_data = {'ulan': ulan, 'scopenote': b_scopenote, 'type': b_type, 'term': b_term}
			ulans.append(getty_data)

	# for queries with multiple results apply some filtering:
	# levenshtein distance
	# todo: query getty for pseudonyms of artist? filter on birth year?
	if len(ulans) > 1:
		d = 100 # declare high value as default and take record with lowest d
		accepted_ulan = None
		for ulan in ulans:
			if ulan['ulan'] is False:
				continue

			dist = distance(artist, ulan['term'])
			if dist < d:
				# set returned record to lowest levenshtein distance
				d = dist

				# don't accept distances that are too high
				if d < 3:
					accepted_ulan = ulan
				else:
					continue

			elif dist == d:
				# TO DO more refining against birthdate or pseudonyms
				# for now don't send anything back if results are ambiguous
				accepted_ulan = None

		if accepted_ulan is None:
			# return empty list of no definitive ulan was found
			ulans = list()
		else:
			ulans = [accepted_ulan]

	return ulans
