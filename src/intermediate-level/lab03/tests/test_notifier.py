from unittest.mock import patch

from app.services import OrderService


@patch("app.services.EmailClient")
def test_send_notification(mock_email):

    service = OrderService()

    service.complete_order("admin@test.com")

    mock_email.return_value.send.assert_called_once_with(
        "admin@test.com", "Su pedido fue completado"
    )
