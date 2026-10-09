import typing

from openvkbottle_types.categories import APICategories
from openvkbottle_types.events import *

API_URL: typing.Final = "https://api.openvk.org/method/"
API_VERSION: typing.Final = "5.86"


__all__ = (
    "API_URL",
    "API_VERSION",
    "APICategories",
    "BaseGroupEvent",
    "BaseUserEvent",
    "Event",
    "GroupEventType",
    "GroupTypes",
    "UserEventType",
    "UserTypes",
)
