from django.shortcuts import render
import re
import operator

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    # words = text.split()
    words = re.findall(r"[\w']+", text)   # Regular Expression
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            # increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1
    
    wordKeySort = sorted(word_dictionary.items())
    wordValueSort = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    percent = []
    for a, b in wordValueSort:
        pctVal = round(int(b) / len(words) * 100, 2)
        percent.append(pctVal)

    wvsLength = len(wordValueSort)
    textWord = [[] for i in range(wvsLength)]
    for i in range(wvsLength):        
        textWord[i].append(wordValueSort[i][0])
        textWord[i].append(wordValueSort[i][1])
        textWord[i].append(percent[i])
    
    return render(request, 'result.html', {'full': text, 'total': len(words), 'textWord': textWord, 'dictionary': word_dictionary.items(), 
        'wordKeySort': wordKeySort, 'wordValueSort': wordValueSort , 'percent': percent})
