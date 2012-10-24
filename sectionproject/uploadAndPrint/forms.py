'''
Created on Oct 18, 2012

This is a document form that appears in the first page.

@author: hunlan
'''
from django import forms

#This is the document form that appears in the first page.
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )