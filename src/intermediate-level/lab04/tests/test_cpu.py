from app.cpu_tasks import calculate


def test_cpu():

    result = calculate()

    assert len(result) == 4
