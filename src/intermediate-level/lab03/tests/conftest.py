import pytest
from app.calculator import OrderCalculator


@pytest.fixture
def calculator():

    return OrderCalculator()
