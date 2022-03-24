# This file is created by -Mohit
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request, ):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    allcaps = request.POST.get('allcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if (removepunc == "on"):
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyze': analyzed}

        djtext=analyzed
    if (allcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Upper Case', 'analyze': analyzed}

        djtext=analyzed
    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char!="\r"):
                analyzed += char
        params = {'purpose': 'Removed NewLine', 'analyze': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Removed extra space', 'analyze': analyzed}

    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            analyzed += 1
        params = {'purpose': 'Character counts ', 'analyze': analyzed}

    if(removepunc!="on" and newlineremove!="on" and extraspaceremover!="on" and charcount!="on" and allcaps!="on"):
        return HttpResponse(''' <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
 <div class="alert alert-info" role="alert">
  Alert!! please choose any option
</div>   ''')
    return render(request, 'analyze.html', params)