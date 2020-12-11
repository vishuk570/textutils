# i have created this file - vishu
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request ,'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')           # get the text
    removepunc = request.POST.get('removepunc', 'off')    # check checkbox value
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')         # check checkbox value
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount', 'off')
    # check which checkbox is on
    if removepunc == "on":
                punchuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
                analyzed=" "
                for char in djtext:
                    if char not in punchuation:
                        analyzed = analyzed + char
                params ={'purpose':'Remove Punc' , 'analyzed_text':analyzed}
                djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext=analyzed

    if (spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc != "on" and fullcaps !="on" and newlineremover !="on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
