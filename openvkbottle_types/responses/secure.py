# noqa: F401,F403
# type: ignore

import openvkbottle_types.codegen.responses.secure
from openvkbottle_types.codegen.responses.secure import *
from openvkbottle_types.responses.base_response import BaseResponse


class SecureSetCounterIntegerResponse(BaseResponse):
    response: int


__all__ = ("SecureSetCounterIntegerResponse",)
__all__ += openvkbottle_types.codegen.responses.secure.__all__
