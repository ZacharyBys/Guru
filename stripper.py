import re
from HTMLParser import HTMLParser

### WILL NEED TO CHANGE FOR PYTHON 3 LATER
### https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def strip_blank_lines(s):
    text = re.sub(r'^$\n', '', s, flags=re.MULTILINE)
    return text

def strip_blank_lines_and_tags(s):
    return strip_blank_lines(strip_tags(s))