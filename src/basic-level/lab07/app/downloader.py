import httpx
from config import BASE_URL


def download_file():
    with httpx.stream(
        "GET",
        f"{BASE_URL}/file",
    ) as response:
        response.raise_for_status()

        with open("downloads/file.txt", "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)

    print("Archivo descargado")
