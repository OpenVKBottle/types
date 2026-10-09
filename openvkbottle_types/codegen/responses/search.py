from openvkbottle_types.base_model import BaseModel, Field
from openvkbottle_types.objects import SearchHint
from openvkbottle_types.responses.base_response import BaseResponse


class SearchGetHintsResponseModel(BaseModel):
    count: int = Field()
    items: list["SearchHint"] = Field()
    suggested_queries: list[str] | None = Field(
        default=None,
    )


class SearchGetHintsResponse(BaseResponse):
    response: "SearchGetHintsResponseModel" = Field()


__all__ = (
    "SearchGetHintsResponse",
    "SearchGetHintsResponseModel",
)
