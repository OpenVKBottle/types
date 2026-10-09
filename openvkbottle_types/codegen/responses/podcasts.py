from openvkbottle_types.base_model import BaseModel, Field
from openvkbottle_types.objects import PodcastExternalData
from openvkbottle_types.responses.base_response import BaseResponse


class PodcastsSearchPodcastResponseModel(BaseModel):
    podcasts: list["PodcastExternalData"] = Field()
    results_total: int = Field()


class PodcastsSearchPodcastResponse(BaseResponse):
    response: "PodcastsSearchPodcastResponseModel" = Field()


__all__ = (
    "PodcastsSearchPodcastResponse",
    "PodcastsSearchPodcastResponseModel",
)
