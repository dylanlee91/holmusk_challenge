import pickle

GOOGLE_AUTH = 'AIzaSyCu02PdP0k7fxqbbn2-z8NIT2IPKbjnuUs'

with open('authkeys', 'wb') as authkeys:
    pickle.dump(GOOGLE_AUTH,authkeys, protocol=pickle.HIGHEST_PROTOCOL)
    authkeys.close()

# to load this:
"""
with open('src\data\keys\authkeys.pickle', 'rb') as handle:
    test = pickle.load(handle)
"""