#!/usr/bin/env python
import os
import sys
'''
This is a django command line script that takes in a file directory
and prints out information about the urls.
'''
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sectionproject.settings")

    from sectionproject.urlutils.urlvalidator.urlvalidator import UrlValidator
    from sectionproject.urlutils.urlcanonicalizer.urlcanonicalizer import UrlCanonicalizer
    from sectionproject.urlutils.urlcomparator.urlcomparator import UrlComparator

    # check input param
    if len(sys.argv) < 2:
        raise Exception('Usage: python ' + sys.argv[0] + ' input-file')
    
    # open file
    infile = open(sys.argv[1])
    
    # store urls in file to a list
    urls = []
    line = infile.readline()
    while len(line) > 0:
        # take out next line characters
        if line.endswith('\n'):
            line = line[:-1]
        urls.append(line)
        line = infile.readline()
    
    # filter out empty strings
    urls = filter(lambda s: s.strip(), urls)
    
    # process each url 
    for url in urls:
        # url valid
        uv = UrlValidator()
        isValid = uv.validate(url)
                
        # remove url in urls
        wo_url_in_urls = urls[:]
        wo_url_in_urls.remove(url)
        
        # initialize param
        normURL = None
        isSrcUnique = UrlComparator.isSourceUnique(url, wo_url_in_urls)
        isNormUnique = None
        
        if isValid:
            uc = UrlCanonicalizer()
            normURL = uc.canonicalizerValidator(uv)
            isNormUnique = UrlComparator.isNormalizeUnique(url, wo_url_in_urls, False)
            
        print 'Source: ' + url
        print 'Valid: ' + str(isValid)
        print 'Canonical: ' + ('None' if normURL == None else normURL)
        print 'Source unique: ' + str(isSrcUnique)
        print 'Canonicalized URL unique: ' + ('N/A' if isNormUnique == None else str(isNormUnique))
        
        print ''
    
    # clean up        
    infile.close()
    
    
    