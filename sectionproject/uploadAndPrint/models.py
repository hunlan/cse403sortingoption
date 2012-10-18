'''
Created on Oct 18, 2012

@author: hunlan
'''
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')