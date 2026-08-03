from app.benchmark import (
    benchmark_async,
    benchmark_cpu,
    benchmark_sync,
)
from app.profiler import profile


def main():

    print("=" * 50)
    print("Benchmark Síncrono")
    benchmark_sync()

    print("=" * 50)
    print("Benchmark Async")
    benchmark_async()

    print("=" * 50)
    print("Benchmark CPU")
    benchmark_cpu()

    print("=" * 50)
    print("Perfilador")
    profile()


if __name__ == "__main__":
    main()
