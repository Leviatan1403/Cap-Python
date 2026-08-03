import cProfile


def profile():

    cProfile.run("benchmark_async()", sort="cumtime")
