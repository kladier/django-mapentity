from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer


class GeoJSONRenderer(JSONRenderer):
    format = 'geojson'
