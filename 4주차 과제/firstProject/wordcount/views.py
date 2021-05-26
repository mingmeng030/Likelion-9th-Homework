from django.shortcuts import render

def home(request):
    return render(request, "home.html")
# Create your views here.
def result(request):
    sentence = request.GET['sentence']
    wordList = text.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return render(request, "result.html", {'fullText': sentence, 'count': len{wordList}, 'wordDict': wordDict.items})
