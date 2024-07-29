# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .chat_completion_response_format import ChatCompletionResponseFormat
from .chat_route_generate_request_agent_tool_choice import (
    ChatRouteGenerateRequestAgentToolChoice,
)
from .common_identifier_safe_unicode import CommonIdentifierSafeUnicode
from .common_logit_bias import CommonLogitBias
from .common_uuid import CommonUuid
from .entries_input_chat_ml_message import EntriesInputChatMlMessage
from .tools_function_tool import ToolsFunctionTool


class ChatRouteGenerateRequestAgent(pydantic_v1.BaseModel):
    messages: typing.List[EntriesInputChatMlMessage] = pydantic_v1.Field()
    """
    A list of new input messages comprising the conversation so far.
    """

    tools: typing.Optional[typing.List[ToolsFunctionTool]] = pydantic_v1.Field(
        default=None
    )
    """
    (Advanced) List of tools that are provided in addition to agent's default set of tools.
    """

    tool_choice: typing.Optional[ChatRouteGenerateRequestAgentToolChoice] = (
        pydantic_v1.Field(default=None)
    )
    """
    Can be one of existing tools given to the agent earlier or the ones provided in this request.
    """

    recall: bool = pydantic_v1.Field()
    """
    Whether previous memories should be recalled or not (will be enabled in a future release)
    """

    remember: bool = pydantic_v1.Field()
    """
    Whether this interaction should form new memories or not (will be enabled in a future release)
    """

    save: bool = pydantic_v1.Field()
    """
    Whether this interaction should be stored in the session history or not
    """

    model: typing.Optional[CommonIdentifierSafeUnicode] = pydantic_v1.Field(
        default=None
    )
    """
    Identifier of the model to be used
    """

    stream: bool = pydantic_v1.Field()
    """
    Indicates if the server should stream the response as it's generated
    """

    stop: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Up to 4 sequences where the API will stop generating further tokens.
    """

    seed: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    If specified, the system will make a best effort to sample deterministically for that particular seed value
    """

    max_tokens: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The maximum number of tokens to generate in the chat completion
    """

    logit_bias: typing.Optional[typing.Dict[str, CommonLogitBias]] = pydantic_v1.Field(
        default=None
    )
    """
    Modify the likelihood of specified tokens appearing in the completion
    """

    response_format: typing.Optional[ChatCompletionResponseFormat] = pydantic_v1.Field(
        default=None
    )
    """
    Response format (set to `json_object` to restrict output to JSON)
    """

    agent: typing.Optional[CommonUuid] = pydantic_v1.Field(default=None)
    """
    Agent ID of the agent to use for this interaction. (Only applicable for multi-agent sessions)
    """

    repetition_penalty: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    length_penalty: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Number between 0 and 2.0. 1.0 is neutral and values larger than that penalize number of tokens generated.
    """

    temperature: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    """

    top_p: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Defaults to 1 An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.
    """

    min_p: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Minimum probability compared to leading token to be considered
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
