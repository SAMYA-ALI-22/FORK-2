# This file was auto-generated by Fern from our API Definition.

import typing

from .docs_hybrid_doc_search_request import DocsHybridDocSearchRequest
from .docs_text_only_doc_search_request import DocsTextOnlyDocSearchRequest
from .docs_vector_doc_search_request import DocsVectorDocSearchRequest

UserDocsSearchRouteSearchRequestBody = typing.Union[
    DocsVectorDocSearchRequest, DocsTextOnlyDocSearchRequest, DocsHybridDocSearchRequest
]
