from googlesearch.googlesearch import GoogleSearch
from stackapi import StackAPI
from prettyprinter import print_formatted_answer
import re

def searchError():
    error = raw_input("Enter the error you want to search:  ")
    error += " Stackoverflow"
    print "Searching the web..."
    response = GoogleSearch().search(error)
    resultUrl = ''
    answerTitle = ''

    foundResult = False
    for result in response.results:
        if (re.search(r'\bstackoverflow\b',result.url)):
            answerTitle = result.title
            resultUrl = result.url
            foundResult = True
            break

    if (not foundResult):
        print "There is no answer to that question. Perhaps seek help from the Oracles"
        return

    print "Found a similar question."
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

    print "Looking for answers..."
    SITE = StackAPI('stackoverflow')
    answers = SITE.fetch('/questions/{ids}/answers', ids=[questionNumber])
    answerList = answers.get('items')

    answerIds = []
    for answer in answerList:
        answerIds.append(answer.get('answer_id'))

    goodAnswers = SITE.fetch('/answers/{ids}', ids=answerIds, filter = 'withbody')
    goodAnswers = goodAnswers.get('items')

    print "Picking best answer..."
    answerAccepted = False
    chosenAnswer = 0
    for i in range (0, len(goodAnswers)):
        if (goodAnswers[i].get('isAccepted') == True):
            answerAccepted = True
            chosenAnswer = i
            break

    if (not answerAccepted):
        currMax = 0
        for j in range (0, len(goodAnswers)):
            currScore = goodAnswers[i].get('score') * goodAnswers[i].get('owner').get('accept_rate')
            if (currScore > currMax):
                currMax = currScore
                chosenAnswer = j

    return print_formatted_answer(answerTitle, goodAnswers[chosenAnswer].get('body'), False)