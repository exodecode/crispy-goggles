import re
import numpy

file1 = open('src.html', 'r')
text = file1.read()
out = ""
for c in text:
    if not c == '\n' and not c == '\r':
        out += c

out1 = re.sub(r">", r">\n", out)

f = open("out.html", "w")
f.write(out1)
f.close()

file2 = open('out.html', 'r')
lines = file2.readlines()
lines = list(filter(lambda x: "<a " in x or "</a>" in x, lines))

new = []
for l in lines:
    new.append(l.strip() if "<a" in l else l)

new = ''.join(new).split('\n')
tracks = []
artists = ''
track = ''
for n in new:
    track_search = re.search(r"track/(.+)\">(.+)</a>", n)
    if(track_search):
        if track != '' and artists != '':
            tracks.append(f'{artists.strip()} - {track}'.replace("&#x27;", "'").replace("&amp;", "&"))
            artists = ''

        track = track_search.group(2)

    artist_search = re.search(r"artist/(.+)\">(.+)</a>", n)
    if(artist_search):
        artist = artist_search.group(2)
        if len(artists) == 0:
            artists = artist
        elif n[0] == ',':
            artists += f', {artist}'

print('\n'.join(tracks))
print(f'\nSongs: {len(tracks)}')
