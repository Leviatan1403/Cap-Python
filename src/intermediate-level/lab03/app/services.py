from app.notifier import EmailClient


class OrderService:
    def __init__(self):
        self.client = EmailClient()

    def complete_order(self, email):

        self.client.send(email, "Su pedido fue completado")

        return True
