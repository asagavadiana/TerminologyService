from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Refbook, RefbookVersion, RefbookElement
from .serializers import RefbookSerializer, RefbookElementSerializer
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from datetime import date

class RefbookListView(ListAPIView):
    serializer_class = RefbookSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date')
        if date:
            date = parse_date(date)
            return Refbook.objects.filter(versions__start_date__lte=date).distinct()
        return Refbook.objects.all()

class RefbookElementListView(APIView):
    def get(self, request, pk):
        version = request.query_params.get('version')
        refbook = get_object_or_404(Refbook, pk=pk)
        if version:
            version_obj = get_object_or_404(RefbookVersion, refbook=refbook, version=version)
        else:
            version_obj = refbook.versions.filter(start_date__lte=date.today()).latest('start_date')
        elements = version_obj.elements.all()
        serializer = RefbookElementSerializer(elements, many=True)
        return Response(serializer.data)

class ValidateRefbookElementView(APIView):
    def get(self, request, pk):
        code = request.query_params.get('code')
        value = request.query_params.get('value')
        version = request.query_params.get('version')
        refbook = get_object_or_404(Refbook, pk=pk)
        if version:
            version_obj = get_object_or_404(RefbookVersion, refbook=refbook, version=version)
        else:
            version_obj = refbook.versions.filter(start_date__lte=date.today()).latest('start_date')
        queryset = RefbookElement.objects.filter(refbook_version=version_obj, code=code, value=value)
        return Response({'valid': queryset.exists()})
