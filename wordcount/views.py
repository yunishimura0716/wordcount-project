from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.htm')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddict = {}
    for w in wordlist:
        if w in worddict:
            worddict[w] += 1
        else:
            worddict[w] = 1
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.htm', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.htm')