from artist_getter import *

assert '500024301' == get_getty_ulan("Stieglitz, Alfred")[0]['ulan']
assert 'Stieglitz, Alfred' == get_getty_artist_name('500024301')
assert 'relationship_type' in get_getty_relationship('500024301')[0]
assert type(get_getty_artist_data('500024301')) is dict
