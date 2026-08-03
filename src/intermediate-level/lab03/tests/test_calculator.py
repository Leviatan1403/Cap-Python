import pytest


@pytest.mark.unit
@pytest.mark.parametrize(
    "subtotal,discount,total",
    [
        (100, 0, 116),
        (100, 10, 104.4),
        (200, 50, 116),
        (100, 100, 0),
    ],
)
def test_total(calculator, subtotal, discount, total):

    assert calculator.calculate_total(subtotal, discount) == total


@pytest.mark.unit
def test_negative_subtotal(calculator):

    with pytest.raises(ValueError):
        calculator.calculate_total(-5, 10)


@pytest.mark.unit
@pytest.mark.parametrize("discount", [-1, 120])
def test_invalid_discount(calculator, discount):

    with pytest.raises(ValueError):
        calculator.calculate_total(100, discount)
