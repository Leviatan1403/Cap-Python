# Funcion con errores

# def calculo (precio: float) -> float:
#     iva = lambda pb, porcen: pb * porcen
#     cantidadIva: float = iva(precio, 1.16)
#     #result = precio + cantidadIva
#     print(f"El precio final es: , {cantidadIva}")

# calculo(510.5)

# Funcion sin Errores


def calculo(precio: float) -> float:
    def iva(pb: float, porcen: float) -> float:
        return pb * porcen

    cantidadIva: float = iva(precio, 1.16)
    # result = precio + cantidadIva
    print(f"El precio final es: , {cantidadIva}")


calculo(510.5)
