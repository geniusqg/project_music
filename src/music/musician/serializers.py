#--*-- coding:utf-8 --*--
from rest_framework import serializers
from models import Musicians


class MusiciansSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Musicians
        fields = ('name', 'letter_index', 'link_url', 'create_time', 'update_time',)
