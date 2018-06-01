from googlesearch.googlesearch import GoogleSearch
from stackapi import StackAPI
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

response = GoogleSearch().search("UnicodeEncodeError: 'charmap' codec can't encode character u'\u2013' in position 8008: character maps to <undefined>")
resultUrl = ''

for result in response.results:
    if (re.search(r'\bstackoverflow\b',result.url)):
        print result.title
        resultUrl = result.url
        break

for i in range(0,len(resultUrl)):
    if (resultUrl[i] == '/'):
        questionNumber = ''
        for j in range(i+1, len(resultUrl)):
            if (resultUrl[j] == '/'):
                break
            questionNumber += resultUrl[j]
        if (questionNumber.isdigit()):
            break

questionNumber = int(questionNumber)

SITE = StackAPI('stackoverflow')
answers = SITE.fetch('/questions/{ids}/answers', ids=[questionNumber])
answerList = answers.get('items')

answerIds = []
for answer in answerList:
    answerIds.append(answer.get('answer_id'))

goodAnswers = SITE.fetch('/answers/{ids}', ids=answerIds, filter = 'withbody')
goodAnswers = goodAnswers.get('items')

firstAnswerBody = goodAnswers[0].get('body')
firstAnswerBody = strip_tags(firstAnswerBody)
print strip_blank_lines(firstAnswerBody)