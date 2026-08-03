class OrderCalculator:
    TAX = 0.16

    def calculate_total(self, subtotal: float, discount: float = 0):

        if subtotal < 0:
            raise ValueError("Subtotal inválido")

        if not 0 <= discount <= 100:
            raise ValueError("Descuento inválido")

        subtotal_discount = subtotal * (1 - discount / 100)

        total = subtotal_discount * (1 + self.TAX)

        return round(total, 2)
