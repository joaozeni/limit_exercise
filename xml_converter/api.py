from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml.etree import ElementTree
from xml_converter.utils import parse_element

class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        root_xml = ElementTree.fromstring(request.data['file'].read())
        
        result = {}
        result[root_xml.tag] = ''
        parced_xml = parse_element(root_xml)
        
        if bool(parced_xml):
            result[root_xml.tag] = parced_xml

        return Response(result)
