import json
from xml.etree import ElementTree
from xml_converter.utils import parse_element

from django.http import JsonResponse
from django.shortcuts import render


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
