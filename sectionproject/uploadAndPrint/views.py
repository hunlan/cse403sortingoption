'''
Created on Oct 18, 2012

@author: hunlan
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from sectionproject.uploadAndPrint.forms import DocumentForm
from sectionproject.uploadAndPrint.models import Document

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            myFile = request.FILES['docfile']
            mystring = '';
            for chunk in myFile.chunks():
                mystring += chunk

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('views.list'))
       
            return HttpResponse(mystring)
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )