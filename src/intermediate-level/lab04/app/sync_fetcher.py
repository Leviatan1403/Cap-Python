import httpx


def fetch_all(urls):

    resultados = []

    with httpx.Client(timeout=10) as client:
        for url in urls:
            response = client.get(url)
            resultados.append(response.json())

    return resultados
