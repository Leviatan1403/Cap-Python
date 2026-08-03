import asyncio

import httpx


async def fetch(client, url, semaphore):

    async with semaphore:
        response = await client.get(url)
        return response.json()


async def fetch_all(urls, limit=5):

    semaphore = asyncio.Semaphore(limit)

    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [fetch(client, url, semaphore) for url in urls]

        return await asyncio.gather(*tasks)
