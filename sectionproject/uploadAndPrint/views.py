'''
Created on Oct 18, 2012

@author: hunlan
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from sectionproject.uploadAndPrint.forms import DocumentForm
from sectionproject.uploadAndPrint.Outputer import outputFile, formatOutput
from sectionproject.uploadAndPrint.InputFile import InputFile
from django.http import HttpResponse, Http404

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            myFile = request.FILES['docfile']
            mystring = '';
            for chunk in myFile.chunks():
                mystring += chunk

            infile = None
            #try:
            infile = InputFile(mystring.__str__())
            #except Exception:
            #    return Http404

            fileOutputString = formatOutput(infile.getSortType(), infile.getUrls())

            return outputFile('outfile.txt', fileOutputString)
    else:
        form = DocumentForm() # A empty, unbound form
        
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )