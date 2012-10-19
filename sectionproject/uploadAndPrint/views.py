'''
Created on Oct 18, 2012

@author: hunlan
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from sectionproject.uploadAndPrint.forms import DocumentForm
from sectionproject.uploadAndPrint.Outputer import outputFile
from sectionproject.uploadAndPrint.InputFile import InputFile
from django.http import HttpResponse, Http404

__PREFIX = 'sorted-'

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Get file from request
            myFile = request.FILES['docfile']
            
            # Get text from file
            mystring = '';
            for chunk in myFile.chunks():
                mystring += chunk

            # Verify that radio button is selected
            if not ('sort' in request.POST):
                print('sort not in request.POST')
                return Http404

            # Try to create inFile object for sorting
            infile = None
            try:
                infile = InputFile(request.POST['sort'], mystring.__str__())
            except Exception:
                return Http404

            # Sort Urls
            sortedUrls = infile.sortUrls()

            # String to Response
            return outputFile(__PREFIX + myFile.name, sortedUrls)
    else:
        form = DocumentForm() # A empty, unbound form
        
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )