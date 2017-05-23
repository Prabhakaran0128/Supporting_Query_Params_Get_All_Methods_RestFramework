# coding: utf-8
"""
Projection  serializers determine the structure of the output that should
be used for  responses.
"""
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework.compat import coreapi, coreschema, template_render

class BaseProjection(object):

    def to_html(self):  # pragma: no cover
        raise NotImplementedError('to_html() must be implemented to display projection controls.')

    def get_results(self, data):
        return data['results']

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        return []


class Proj(BaseProjection):
    """
    A simple proj based on json based style that supports output as
    query parameters. For example:

    http://api.example.org/accounts/?proj={"Name" : 1}
    """


    # Client can control the json proj using this query parameter.
    proj_param = 'proj'
    proj_description = ('Projection Input as JSON to filter')
    

    # Client can control the proj input as json(string) this query parameter.

    # Set to an String .
    # Only relevant if 'proj_param' has also been set.


    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        fields = [
            coreapi.Field(
                name=self.proj_param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title='Projection',
                    description=force_text(self.proj_description)
                )
            )
        ]
        return fields