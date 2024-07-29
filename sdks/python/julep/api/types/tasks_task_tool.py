# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .common_valid_python_identifier import CommonValidPythonIdentifier
from .tools_function_def import ToolsFunctionDef
from .tools_tool_type import ToolsToolType


class TasksTaskTool(pydantic_v1.BaseModel):
    inherited: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Read-only: Whether the tool was inherited or not. Only applies within tasks.
    """

    type: ToolsToolType = pydantic_v1.Field()
    """
    Whether this tool is a `function`, `api_call`, `system` etc. (Only `function` tool supported right now)
    """

    name: CommonValidPythonIdentifier = pydantic_v1.Field()
    """
    Name of the tool (must be unique for this agent and a valid python identifier string )
    """

    function: typing.Optional[ToolsFunctionDef] = None
    integration: typing.Optional[typing.Any] = None
    system: typing.Optional[typing.Any] = None
    api_call: typing.Optional[typing.Any] = None

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
