from openvkbottle_types.base_model import Field
from openvkbottle_types.objects import StorageValue
from openvkbottle_types.responses.base_response import BaseResponse


class StorageGetKeysResponse(BaseResponse):
    response: list[str] = Field()


class StorageGetResponse(BaseResponse):
    response: list["StorageValue"] = Field()


__all__ = (
    "StorageGetKeysResponse",
    "StorageGetResponse",
)
