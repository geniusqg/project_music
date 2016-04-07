#--*-- coding:utf-8 --*--


from models import Musicians
from serializers import MusiciansSerializer
from rest_framework import viewsets


class MusiciansViewSet(viewsets.ModelViewSet):

    queryset = Musicians.objects.all()
    serializer_class = MusiciansSerializer
