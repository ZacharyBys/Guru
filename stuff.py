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

def print_formatted_answer(title, answer):
    print ' '
    print '|)-------------------------------------------------------------(|'
    print title
    print '|)-------------------------------------------------------------(|'

    formattedAnswer = strip_blank_lines(strip_tags(answer))
    lines = formattedAnswer.splitlines()

    maxLine = 0
    for line in lines:
        if (len(line) > maxLine):
            maxLine = len(line)
    delimiter = ''
    for i in range (0, maxLine+4):
        delimiter = delimiter + '*'

    print delimiter
    
    newLines = []
    for line in lines:
        newLine = line
        for i in range (len(newLine), maxLine+1):
            newLine = newLine + ' '
        newLine = newLine + '|'
        newLines.append(newLine)
    for line in newLines:
        print '| ' + line

    print delimiter


error = raw_input("Enter the error you want to search:  ")
response = GoogleSearch().search(error)
resultUrl = ''
answerTitle = ''

for result in response.results:
    if (re.search(r'\bstackoverflow\b',result.url)):
        answerTitle = result.title
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

print_formatted_answer(answerTitle, goodAnswers[0].get('body'))