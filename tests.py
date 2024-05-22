import getty_getter.getty_getter as getty

assert '500024301' == getty.get_getty_ulan("Stieglitz, Alfred")[0]['ulan']
assert 'Stieglitz, Alfred' == getty.get_getty_artist_name('500024301')
assert 'relationship_type' in getty.get_getty_relationship('500024301')[0]
