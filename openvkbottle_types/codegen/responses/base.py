import typing

from openvkbottle_types.base_model import BaseEnumMeta, Field, IntEnum
from openvkbottle_types.objects import BaseUploadServer
from openvkbottle_types.responses.base_response import BaseResponse


class BaseBoolResponse(BaseResponse):
    response: bool = Field()


class BaseGetUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class BaseOkResponseModel(IntEnum, metaclass=BaseEnumMeta):
    OK = 1


class BaseOkResponse(BaseResponse):
    response: "BaseOkResponseModel" = Field(default=BaseOkResponseModel.OK)


class BaseUndefinedResponse(BaseResponse):
    response: dict[str, typing.Any] = Field()


__all__ = (
    "BaseBoolResponse",
    "BaseGetUploadServerResponse",
    "BaseOkResponse",
    "BaseOkResponseModel",
    "BaseUndefinedResponse",
)
