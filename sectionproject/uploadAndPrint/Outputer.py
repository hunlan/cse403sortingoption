'''
Created on Oct 18, 2012

@author: hunlan
'''
from django.http import HttpResponse
import csv

def outputFile(filename, list_content):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/plain')
    response['Content-Disposition'] = 'attachment; filename=' + filename


    writer = csv.writer(response)
    for s in list_content :
        writer.writerow([s])
    return response
