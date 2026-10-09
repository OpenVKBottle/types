from openvkbottle_types.base_model import Field
from openvkbottle_types.objects import StatusStatus
from openvkbottle_types.responses.base_response import BaseResponse


class StatusGetResponse(BaseResponse):
    response: "StatusStatus" = Field()


__all__ = ("StatusGetResponse",)
