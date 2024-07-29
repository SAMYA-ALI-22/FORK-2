# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .agents_update_agent_request_default_settings import (
    AgentsUpdateAgentRequestDefaultSettings,
)
from .agents_update_agent_request_instructions import (
    AgentsUpdateAgentRequestInstructions,
)
from .common_identifier_safe_unicode import CommonIdentifierSafeUnicode


class AgentsUpdateAgentRequest(pydantic_v1.BaseModel):
    """
    Payload for updating a agent
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: CommonIdentifierSafeUnicode = pydantic_v1.Field()
    """
    Name of the agent
    """

    about: str = pydantic_v1.Field()
    """
    About the agent
    """

    model: str = pydantic_v1.Field()
    """
    Model name to use (gpt-4-turbo, gemini-nano etc)
    """

    instructions: AgentsUpdateAgentRequestInstructions = pydantic_v1.Field()
    """
    Instructions for the agent
    """

    default_settings: typing.Optional[AgentsUpdateAgentRequestDefaultSettings] = (
        pydantic_v1.Field(default=None)
    )
    """
    Default settings for all sessions created by this agent
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        kwargs_with_defaults_exclude_none: typing.Any = {
            "by_alias": True,
            "exclude_none": True,
            **kwargs,
        }

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset),
            super().dict(**kwargs_with_defaults_exclude_none),
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
