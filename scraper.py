import re

file1 = open('src.html', 'r')
text = file1.read().replace('\n', '').replace('\r', '').replace('</a>', '</a>\n').split('\n')
artists = []
artist = ""

for line in text:
    a = re.search(r"><a href=\"/artist/.*?\">(.+?)</a>", line)
    if artist != "" and a:
        artists.append(artist)
        artist = ""

    if artist == "" and a:
        artist = a.group(1)

    oa = re.search(r", <a href=\"/artist/.*?\">(.+?)</a>", line)
    if oa:
        artist = f'{artist}, {oa.group(1)}'

tracks = re.findall(r"<a .*? href=\"/track/.*?\">(.+?)</a>", ''.join(text))
print('\n'.join(map(lambda x: f'{x[0]} - {x[1]}'.replace("&#x27;", "'"), zip(artists, tracks))))
