'''
Created on Oct 18, 2012

@author: hunlan
'''
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )