from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from getty import getty_scraper
import json

# Create your views here.

class GetUlanView(View):
	def get(self, request):

		artist_ulan = getty_scraper.get_getty_ulan(u"Stieglitz, Alfred")

		return HttpResponse(artist_ulan, content_type="application/json")

class GetArtistRelationshipsView(View):
	def get(self, request):

		artist_relationships = getty_scraper.get_getty_relationship("500024301")

		return HttpResponse(artist_relationships, content_type="application/json")