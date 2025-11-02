from curses import wrapper
from app import App

from ytmusicapi import YTMusic

# no args => uses default (unauthenticated) headers; works for public searches
yt = YTMusic()

results = yt.search("Daft Punk Get Lucky", filter="songs", limit=10)
for r in results:
    # result may be type 'song', 'video', 'artist', etc.
    print(r.get("title"), "-", r.get("artist"))

app = App()
wrapper(app.wrapper)

