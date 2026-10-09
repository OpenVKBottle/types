# type: ignore
# noqa: F401,F403

import openvkbottle_types.codegen.responses.wall
from openvkbottle_types.base_model import Field
from openvkbottle_types.codegen.responses.wall import *
from openvkbottle_types.objects import WallWallpostFull


class WallGetByIdExtendedResponseModel(WallGetByIdExtendedResponseModel):
    items: list[WallWallpostFull] = Field()


class WallGetByIdExtendedResponse(WallGetByIdExtendedResponse):
    response: WallGetByIdExtendedResponseModel = Field()


class WallGetByIdResponseModel(WallGetByIdResponseModel):
    items: list[WallWallpostFull] | None = Field(
        default=None,
    )


class WallGetByIdResponse(WallGetByIdResponse):
    response: WallGetByIdResponseModel = Field()


class WallGetExtendedResponseModel(WallGetExtendedResponseModel):
    items: list[WallWallpostFull] = Field()


class WallGetExtendedResponse(WallGetExtendedResponse):
    response: WallGetExtendedResponseModel = Field()


class WallGetResponseModel(WallGetResponseModel):
    items: list[WallWallpostFull] = Field()


class WallGetResponse(WallGetResponse):
    response: WallGetResponseModel = Field()


class WallSearchExtendedResponseModel(WallSearchExtendedResponseModel):
    items: list[WallWallpostFull] = Field()


class WallSearchExtendedResponse(WallSearchExtendedResponse):
    response: WallSearchExtendedResponseModel = Field()


class WallSearchResponseModel(WallSearchResponseModel):
    items: list[WallWallpostFull] = Field()


class WallSearchResponse(WallSearchResponse):
    response: WallSearchResponseModel = Field()


__all__ = openvkbottle_types.codegen.responses.wall.__all__
