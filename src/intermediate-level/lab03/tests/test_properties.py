from app.calculator import OrderCalculator
from hypothesis import given
from hypothesis import strategies as st

calculator = OrderCalculator()


@given(
    subtotal=st.floats(min_value=0, max_value=100000),
    discount=st.floats(min_value=0, max_value=100),
)
def test_total_never_negative(subtotal, discount):

    total = calculator.calculate_total(subtotal, discount)

    assert total >= 0


@given(subtotal=st.floats(min_value=0, max_value=100000))
def test_discount_reduces_total(subtotal):

    total1 = calculator.calculate_total(subtotal, 0)

    total2 = calculator.calculate_total(subtotal, 20)

    assert total2 <= total1
