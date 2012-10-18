'''
Created on Oct 18, 2012

@author: hunlan
'''
from django.http import HttpResponse
import csv

def outputFile(filename, content):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    writer = csv.writer(response)
    writer.writerow([content])

    return response

def formatOutput(sortType, list):
    retString = sortType
    
    for s in list:
        retString += '\n' + s
    
    return retString