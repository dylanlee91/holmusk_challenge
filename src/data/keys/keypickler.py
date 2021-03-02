import pickle

GOOGLE_AUTH = 'AIzaSyBwRUBjZERFC2LUNXK28KXdPo4r0i8jgTc'

with open('authkeys', 'wb') as authkeys:
    pickle.dump(GOOGLE_AUTH,authkeys, protocol=pickle.HIGHEST_PROTOCOL)
    authkeys.close()

# to load this:
"""
with open('src\data\keys\authkeys.pickle', 'rb') as handle:
    test = pickle.load(handle)
"""