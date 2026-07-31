import httpx
from config import BASE_URL, TIMEOUT
from retry import retry_policy


class ApiClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=TIMEOUT, http2=True)

    @retry_policy
    def get_users(self):
        response = self.client.get("/users")

        response.raise_for_status()

        return response.json()

    @retry_policy
    def get_error(self):
        response = self.client.get("/error")

        response.raise_for_status()

        return response.text

    @retry_policy
    def get_slow(self):
        response = self.client.get("/slow")

        response.raise_for_status()

        return response.json()
