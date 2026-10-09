from openvkbottle_types.base_model import BaseModel, Field
from openvkbottle_types.objects import BaseStickerNew, StoreProduct, StoreStickersKeyword
from openvkbottle_types.responses.base_response import BaseResponse


class StoreGetFavoriteStickersResponseModel(BaseModel):
    count: int = Field()
    items: list["BaseStickerNew"] = Field()


class StoreGetFavoriteStickersResponse(BaseResponse):
    response: "StoreGetFavoriteStickersResponseModel" = Field()


class StoreGetProductsResponseModel(BaseModel):
    items: list["StoreProduct"] = Field()
    count: int = Field()


class StoreGetProductsResponse(BaseResponse):
    response: "StoreGetProductsResponseModel" = Field()


class StoreGetStickersKeywordsResponseModel(BaseModel):
    count: int = Field()
    dictionary: list["StoreStickersKeyword"] = Field()
    chunks_count: int | None = Field(
        default=None,
    )
    chunks_hash: str | None = Field(
        default=None,
    )


class StoreGetStickersKeywordsResponse(BaseResponse):
    response: "StoreGetStickersKeywordsResponseModel" = Field()


__all__ = (
    "StoreGetFavoriteStickersResponse",
    "StoreGetFavoriteStickersResponseModel",
    "StoreGetProductsResponse",
    "StoreGetProductsResponseModel",
    "StoreGetStickersKeywordsResponse",
    "StoreGetStickersKeywordsResponseModel",
)
