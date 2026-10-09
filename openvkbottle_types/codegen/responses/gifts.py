from openvkbottle_types.base_model import BaseModel, Field
from openvkbottle_types.objects import GiftsGift
from openvkbottle_types.responses.base_response import BaseResponse


class GiftsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["GiftsGift"] = Field()


class GiftsGetResponse(BaseResponse):
    response: "GiftsGetResponseModel" = Field()


__all__ = (
    "GiftsGetResponse",
    "GiftsGetResponseModel",
)
