# coding: utf-8
"""
Query serializers determine the structure of the output that should
be used for  responses.
"""
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework.compat import coreapi, coreschema, template_render



class BaseQuery(object):


    def to_html(self):  # pragma: no cover
        raise NotImplementedError('to_html() must be implemented to display query based json controls.')

    def get_results(self, data):
        return data['results']

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        return []


class Query(BaseQuery):
    """
    A simple query based on json based style that supports output as
    query parameters. For example:

    http://api.example.org/accounts/?query={"Name" : "PP"}
    """


    # Client can control the json query using this query parameter.
    query_param = 'query'
    query_description = _('Query Input as JSON to filter')

    # Client can control the query input as json(string) this query parameter.

    # Set to an String .
    # Only relevant if 'query_param' has also been set.


    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        fields = [
            coreapi.Field(
                name=self.query_param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title='Query',
                    description=force_text(self.query_description)
                )
            )
        ]
        return fields