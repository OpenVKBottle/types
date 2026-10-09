from openvkbottle_types.base_model import Field
from openvkbottle_types.objects import StatsPeriod, StatsWallpostStat
from openvkbottle_types.responses.base_response import BaseResponse


class StatsGetPostReachResponse(BaseResponse):
    response: list["StatsWallpostStat"] = Field()


class StatsGetResponse(BaseResponse):
    response: list["StatsPeriod"] = Field()


__all__ = (
    "StatsGetPostReachResponse",
    "StatsGetResponse",
)
