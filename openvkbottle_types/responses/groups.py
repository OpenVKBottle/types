# noqa: F401,F403
# type: ignore

import openvkbottle_types.codegen.responses.groups
from openvkbottle_types.codegen.responses.groups import *
from openvkbottle_types.objects import GroupsMemberRole, GroupsUserXtrRole
from openvkbottle_types.responses.base_response import BaseResponse


class GetMembersFilterManagersResponseModel(BaseResponse):
    count: int | None = None
    items: list[GroupsMemberRole] | None = None


class GetMembersFieldsFilterManagersResponseModel(BaseResponse):
    count: int | None = None
    items: list[GroupsUserXtrRole] | None = None


class GetMembersFilterManagersResponse(BaseResponse):
    response: GetMembersFilterManagersResponseModel


class GetMembersFieldsFilterManagersResponse(BaseResponse):
    response: GetMembersFieldsFilterManagersResponseModel


__all__ = (
    "GetMembersFieldsFilterManagersResponse",
    "GetMembersFieldsFilterManagersResponseModel",
    "GetMembersFilterManagersResponse",
    "GetMembersFilterManagersResponseModel",
)
__all__ += openvkbottle_types.codegen.responses.groups.__all__  # type: ignore
