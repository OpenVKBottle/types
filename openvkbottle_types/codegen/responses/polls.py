from openvkbottle_types.base_model import Field
from openvkbottle_types.objects import PollsBackground, PollsFieldsVoters, PollsPoll, PollsPollExtended, PollsVoters
from openvkbottle_types.responses.base_response import BaseResponse


class PollsCreateResponse(BaseResponse):
    response: "PollsPoll" = Field()


class PollsGetBackgroundsResponse(BaseResponse):
    response: list["PollsBackground"] = Field()


class PollsGetByIdResponse(BaseResponse):
    response: "PollsPollExtended" = Field()


class PollsGetVotersFieldsResponse(BaseResponse):
    response: list["PollsFieldsVoters"] = Field()


class PollsGetVotersResponse(BaseResponse):
    response: list["PollsVoters"] = Field()


class PollsSavePhotoResponse(BaseResponse):
    response: "PollsBackground" = Field()


__all__ = (
    "PollsCreateResponse",
    "PollsGetBackgroundsResponse",
    "PollsGetByIdResponse",
    "PollsGetVotersFieldsResponse",
    "PollsGetVotersResponse",
    "PollsSavePhotoResponse",
)
