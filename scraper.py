import re

file1 = open('src.html', 'r')
text = file1.read().replace('\n', '').replace('\r', '')
artists = re.findall(r"(?<!,) <a href=\"/artist/.*?\">(.+?)</a>", text)
tracks = re.findall(r"<a .*? href=\"/track/.*?\">(.+?)</a>", text)

print('\n'.join(map(lambda x: f'{x[0]} - {x[1]}'.replace("&#x27;", "'"), zip(artists, tracks))))
