import httpx

BASE_URL = "http://localhost:8080"

TIMEOUT = httpx.Timeout(
    connect=2.0,
    read=2.0,
    write=2.0,
    pool=2.0,
)
