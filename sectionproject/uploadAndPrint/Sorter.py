'''
Created on Oct 18, 2012

@author: hunlan
'''

def GodSort(urls):
    return urls

def MergeSort(urls):
    return urls

def HeapSort(urls):
    return urls

def InsertSort(urls):
    sorted_urls = [urls.pop()]
    for url in urls:
        for i in range(0, len(sorted_urls)):
            if url < sorted_urls[i]:
                sorted_urls.insert(i, url)
                break
            if i == len(sorted_urls) - 1:
                sorted_urls.append(url)
    return sorted_urls