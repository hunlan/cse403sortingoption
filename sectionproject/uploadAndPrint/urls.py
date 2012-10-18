'''
Created on Oct 18, 2012

@author: hunlan
'''

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('sectionproject.uploadAndPrint.views',
    url(r'^list/$', 'list', name='list'),
)