
class Jugador:
    def __init__(self, dni, balance):
        self.dni = dni
        self.balance = balance
        self.tamaño_apuesta = 1.00
        self.ultimo_pago = 0.00
        self.total_ganado = 0.00
        self.total_apuesta = 0.00

    def get_datos(self):
        datos_jugador = {"balance": "{:.2f}".format(self.balance),
                         "tamaño_apuesta": "{:.2f}".format(self.tamaño_apuesta),
                         "ultimo_pago": "{:.2f}".format(self.ultimo_pago) if self.ultimo_pago else "N/A",
                         "total_ganado": "{:.2f}".format(self.total_ganado),
                         "total_apuesta": "{:.2f}".format(self.total_apuesta)
                         }
        return datos_jugador

    def poner_apuesta(self):
        apuesta = self.tamaño_apuesta
        self.balance -= apuesta
        self.total_apuesta += apuesta