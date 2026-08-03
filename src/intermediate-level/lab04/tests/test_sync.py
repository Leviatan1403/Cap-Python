from app.config import URLS
from app.sync_fetcher import fetch_all


def test_sync():

    data = fetch_all(URLS)

    assert len(data) == len(URLS)
