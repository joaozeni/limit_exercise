import json

from django.http import JsonResponse
from django.shortcuts import render

from xml.etree import ElementTree

def parse_element(element):
    result = []
    
    for sub_element in element:
        data = {}
        data[sub_element.tag] = sub_element.text
        if list(sub_element):
            data[sub_element.tag] = parse_element(sub_element)
        result.append(data)
    
    return result


def upload_page(request):
    if request.method == 'POST':
        root_xml = ElementTree.fromstring(request.FILES['file'].read())
        
        result = {}
        result[root_xml.tag] = ''
        parced_xml = parse_element(root_xml)
        
        if bool(parced_xml):
            result[root_xml.tag] = parced_xml
        
        return JsonResponse(result)

    return render(request, "upload_page.html")
