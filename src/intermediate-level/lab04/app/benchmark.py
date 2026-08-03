import asyncio
import time

from app.async_fetcher import fetch_all as async_fetch
from app.config import URLS
from app.cpu_tasks import calculate
from app.sync_fetcher import fetch_all as sync_fetch


def benchmark_sync():

    start = time.perf_counter()

    sync_fetch(URLS)

    end = time.perf_counter()

    print(f"Síncrono: {end - start:.3f} segundos")


def benchmark_async():

    start = time.perf_counter()

    asyncio.run(async_fetch(URLS))

    end = time.perf_counter()

    print(f"Async: {end - start:.3f} segundos")


def benchmark_cpu():

    start = time.perf_counter()

    calculate()

    end = time.perf_counter()

    print(f"CPU ProcessPool: {end - start:.3f} segundos")
