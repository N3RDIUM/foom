from ytmusicapi import YTMusic
import json

yt = YTMusic()

results = yt.search("Daft Punk Get Lucky", filter="songs")
for r in results:
    print(json.dumps(r, indent=4))

