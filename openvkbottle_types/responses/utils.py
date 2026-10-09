# type: ignore
# noqa: F401,F403

import typing

import openvkbottle_types.codegen.responses.utils
from openvkbottle_types.base_model import Field
from openvkbottle_types.codegen.responses.utils import *
from openvkbottle_types.objects import UtilsDomainResolved
from openvkbottle_types.responses.base_response import BaseResponse


class UtilsResolveScreenNameResponse(BaseResponse):
    response: UtilsDomainResolved | list[typing.Any] = Field(
        default_factory=lambda: [],
    )


__all__ = ("UtilsResolveScreenNameResponse",)
__all__ += openvkbottle_types.codegen.responses.utils.__all__
