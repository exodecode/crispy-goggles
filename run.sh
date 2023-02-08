#!/bin/bash
# NAME=${1?Error: no name given}
# echo "Hello! $NAME"
LINK=${1?Error: no playlist url given}
wget $LINK -O src.html
# touch pretty.html
#tidy out.html > pretty.html

python scraper.py
