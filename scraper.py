import re
import numpy
# Using readlines()
file1 = open('pretty.html', 'r')

lines = file1.readlines()
artist = ""
album = ""

track_lines = []
for line in lines:
    a = re.search(r"Album by (.+)", line)
    al = re.search(r"<title>(.+) - Album by", line)
    if(a):
        artist = a.group(1)[0:-2]
    if(al):
        album = al.group(1)

    t = re.search(r"track (.+?)\">", line)

    if(t):
        track_lines.append(f'{artist} - {t.group(1).replace("&amp;", "&")}')

track_lines = track_lines[1::2]

print(f"{artist} - {album}\n")
print("\n".join(track_lines))
print(f"\nSong Count: {len(track_lines)}")

