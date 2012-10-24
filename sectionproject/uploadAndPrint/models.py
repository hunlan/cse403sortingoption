'''
Created on Oct 18, 2012

Simple database model for the documents.  
Currently not used, but its just a good thing
to have a model, view, url, test for each application

TODO: To make this class to work, need to setup database
in settings.py

@author: hunlan
'''
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')