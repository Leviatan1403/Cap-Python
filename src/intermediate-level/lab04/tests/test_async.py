import pytest
from app.async_fetcher import fetch_all
from app.config import URLS


@pytest.mark.asyncio
async def test_async():

    data = await fetch_all(URLS)

    assert len(data) == len(URLS)
