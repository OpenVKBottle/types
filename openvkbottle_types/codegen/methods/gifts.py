import typing

from openvkbottle_types.methods.base_category import BaseCategory
from openvkbottle_types.objects import *
from openvkbottle_types.responses.gifts import *  # noqa: F401,F403  # type: ignore


class GiftsCategory(BaseCategory):
    async def get(
        self,
        count: int | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> GiftsGetResponseModel:
        """Method `gifts.get()`

        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("gifts.get", params)
        model = GiftsGetResponse
        return model(**response).response


__all__ = ("GiftsCategory",)
