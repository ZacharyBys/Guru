from stripper import strip_blank_lines_and_tags
import re
import click

def print_formatted_answer(title, answer, useDelimitters):
    print ' '
    titleDelimiter = '|)'
    for i in range (0, len(title)):
        titleDelimiter = titleDelimiter + '-'
    titleDelimiter = titleDelimiter + '(|'

    print titleDelimiter
    print '| ' + title + ' |'
    print titleDelimiter

    formattedAnswer = strip_blank_lines_and_tags(answer)
    lines = formattedAnswer.splitlines()

    if (useDelimitters):
        maxLine = 0
        for line in lines:
            if (len(line) > maxLine):
                maxLine = len(line)
        delimiter = ''
        for i in range (0, maxLine+4):
            delimiter = delimiter + '*'

        print delimiter
    
    if (useDelimitters):
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
    else:
        for line in lines:
            print line
        print ' '
