import sys
import markdown

with open(sys.argv[2], "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text,extensions=['extra','codehilite','sane_lists','toc'])

with open(sys.argv[3], 'w', encoding="utf-8", errors="xmlcharrefreplace") as f:
    f.write(html)