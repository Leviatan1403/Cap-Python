from app.calculator import OrderCalculator


def test_25_percent_discount():

    calc = OrderCalculator()

    total = calc.calculate_total(400, 25)

    assert total == 348
