#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import django

reload(sys)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

import json
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# snippet = Snippet(code='foo = "bar"\n')
# snippet.save()
#
# snippet = Snippet(code='print "hello, world"\n')
# snippet.save()

snippet = Snippet.objects.get(id=12)
# serializer = SnippetSerializer(snippet)
# data = serializer.data
# print data

# print type(json.dumps(data))
# print json.dumps(data)

# import io
# content = JSONRenderer().render(serializer.data)
# stream = io.BytesIO(content)
# data = JSONParser().parse(stream)
# print data
# print type(json.dumps(data))
# print json.dumps(data)

data = {u'style': u'friendly', u'code': u'echfdsfsdfo123', u'language': u'python', u'title': u'dflkjdsfl', u'linenos': False}
serializer = SnippetSerializer(snippet, data=data)
serializer.is_valid()
serializer.validated_data
serializer.save()

# serializer = SnippetSerializer(Snippet.objects.all(), many=True)
# data = serializer.data
# print(data)

# from snippets.serializers import SnippetSerializer
# serializer = SnippetSerializer()
# print(repr(serializer))
# # SnippetSerializer():