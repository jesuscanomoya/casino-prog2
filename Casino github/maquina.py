import random
import pygame
from interfaz import *
from ajustes import *
from jugador2 import Jugador
class MaquinaBlackjack:
    """
    Representa la máquina de juego de Blackjack.

    Esta clase maneja el estado y la lógica del juego de Blackjack, incluyendo las manos del jugador y del crupier,
    el saldo del jugador, y la interacción con la interfaz de usuario.

    Parameters
    ----------
    pantalla : pygame.Surface
        La superficie de Pygame donde se renderizará el juego.

    Attributes
    ----------
    pantalla : pygame.Surface
        La superficie de Pygame donde se renderiza el juego.
    mano_jugador : list of tuple
        La mano del jugador, representada como una lista de tuplas (valor, palo).
    mano_crupier : list of tuple
        La mano del crupier, representada como una lista de tuplas (valor, palo).
    saldo : int
        El saldo del jugador, inicializado en 10.
    interfaz : Interfaz
        Una instancia de la clase Interfaz para manejar la interacción con el usuario.
    pedir_carta_jugador : bool
        Bandera que indica si el jugador ha solicitado una carta.
    carta_oculta : bool
        Bandera que indica si la segunda carta del crupier está oculta.
    """

    def __init__(self, pantalla,jugador):
        """
        Inicializa una nueva instancia de MaquinaBlackjack.

        Parameters
        ----------
        pantalla : pygame.Surface
            La superficie de Pygame donde se renderizará el juego.
        """
        self.pantalla = pantalla
        self.mano_jugador = []
        self.mano_crupier = []
        self.curr_jugador = jugador
        self.interfaz = Interfaz(pantalla)  # Creamos una instancia de la clase Interfaz
        self.pedir_carta_jugador = False
        self.carta_oculta = True
        self.sonido_carta = pygame.mixer.Sound("imagenes_cartas/sonido_carta.mp3")
        self.sonido_carta.set_volume(0.1)

    def calcular_puntuacion(self, mano):
        """
        Calcula la puntuación total de una mano en el juego de Blackjack.

        La puntuación se calcula sumando los valores de las cartas en la mano. Los ases ('A') se consideran como 11 puntos,
        pero si la puntuación total supera 21, se restan 10 puntos por cada as hasta que la puntuación sea válida o no queden ases.
        Las cartas con figuras ('J', 'Q', 'K') se consideran como 10 puntos.

        Parameters
        ----------
        mano : list of tuple
            La mano del jugador o del crupier. Cada carta es una tupla con el valor y el palo.

        Returns
        -------
        int
            La puntuación total de la mano.
        """

        puntuacion = 0
        ases = 0
        for carta in mano:
            valor = carta[0]
            if valor == 'A':
                ases += 1
                puntuacion += 11
            elif valor in ['J', 'Q', 'K']:
                puntuacion += 10
            else:
                puntuacion += int(valor)

        while puntuacion > 21 and ases:
            puntuacion -= 10
            ases -= 1

        return puntuacion

    def pedir_carta(self, mano):
        """
        Añade una carta aleatoria a la mano proporcionada.

        Selecciona una carta aleatoria basada en los valores y palos disponibles, y la añade a la mano especificada.
        La carta es representada como una tupla (valor, palo).

        Parameters
        ----------
        mano : list of tuple
            La mano del jugador o del crupier a la cual se le añadirá una nueva carta. Cada carta es una tupla con el valor y el palo.

        Returns
        -------
        list of tuple
            La mano actualizada con la nueva carta añadida.
        """

        carta = (random.choice(valores), random.choice(palos))
        mano.append(carta)

        return mano


    def mostrar_mano(self):
        """
        Muestra las manos del jugador y del crupier en la pantalla del juego.

        Utiliza imágenes de las cartas correspondientes para representar las manos del jugador y del crupier.
        Las imágenes de las cartas se cargan desde archivos PNG y se dibujan en la pantalla utilizando Pygame.
        La segunda carta del crupier puede estar oculta dependiendo del estado del juego.
        """

        # Mostrar la mano del jugador
        for i, carta in enumerate(self.mano_jugador):
            imagen_carta = pygame.image.load(f"imagenes_cartas/{carta[0]}_{carta[1]}.png")
            self.pantalla.blit(imagen_carta, (x_jugador + i * 100, y_jugador))

        # Mostrar la mano del crupier
        for i, carta in enumerate(self.mano_crupier):
            if i == 0 and self.carta_oculta:
                imagen_carta = pygame.image.load(carta_oculta)
            else:
                imagen_carta = pygame.image.load(f"imagenes_cartas/{carta[0]}_{carta[1]}.png")
            self.pantalla.blit(imagen_carta, (x_crupier + i * 100, y_crupier))

        pygame.display.update()

    def comparar_mano(self):
        """
        Compara las manos del jugador y del crupier para determinar el resultado del juego de Blackjack.

        Calcula las puntuaciones de las manos del jugador y del crupier utilizando el método `calcular_puntuacion`.
        Luego, determina el resultado del juego basado en las reglas de Blackjack.

        Returns
        -------
        str
            El resultado del juego. Puede ser uno de los siguientes valores:
            - 'BLACKJACK': Si la puntuación del jugador es 21.
            - 'Has perdido': Si la puntuación del jugador es mayor a 21 o es menor que la puntuación del crupier.
            - 'Has ganado': Si la puntuación del crupier es mayor a 21 o la puntuación del jugador es mayor que la del crupier.
            - 'Hay empate': Si la puntuación del jugador es igual a la puntuación del crupier.
        """

        puntuacion_jugador = self.calcular_puntuacion(self.mano_jugador)
        puntuacion_crupier = self.calcular_puntuacion(self.mano_crupier)

        if puntuacion_jugador == 21:
            resultado = 'BLACKJACK'
        elif puntuacion_jugador > 21:
            resultado = 'Has perdido'
        elif puntuacion_crupier > 21:
            resultado = 'Has ganado'
        elif puntuacion_jugador == puntuacion_crupier:
            resultado = 'Hay empate'
        elif puntuacion_jugador > puntuacion_crupier:
            resultado = 'Has ganado'
        else:
            resultado = 'Has perdido'

        return resultado


    def turno_jugador(self, mano_crupier_provisional):
        """
        Gestiona el turno del jugador en el juego de Blackjack.

        Durante el turno del jugador, se permite que el jugador pida cartas mientras su puntuación sea menor que 21.
        La interfaz se actualiza continuamente para reflejar los cambios en la mano del jugador y la puntuación provisional del crupier.

        Parameters
        ----------
        mano_crupier_provisional : list of tuple
            La mano provisional del crupier, utilizada para mostrar la puntuación parcial del crupier durante el turno del jugador.
        """

        seguir = True
        while seguir and self.calcular_puntuacion(self.mano_jugador) < 21:
            if self.pedir_carta_jugador:  # Solo pedir carta si el jugador ha pedido una
                self.pedir_carta(self.mano_jugador)
                self.interfaz.limpiar_elementos(self.curr_jugador.balance)
                self.interfaz.draw_buttons()
                self.interfaz.actualizar_puntuacion(self.calcular_puntuacion(mano_crupier_provisional), self.calcular_puntuacion(self.mano_jugador))
                self.mostrar_mano()
                self.pedir_carta_jugador = False  # Reiniciar el flag
            opcion = self.interfaz.handle_events()
            if opcion == 'pedir_carta':
                self.pedir_carta_jugador = True  # Marcar que el jugador ha pedido una carta
                self.sonido_carta.play()
            elif opcion == 'turno_crupier':
                seguir = False



    def turno_crupier(self):
        """
        Gestiona el turno del crupier en el juego de Blackjack.

        El crupier sigue tomando cartas hasta que su puntuación sea mayor de 16. Durante el turno del crupier,
        se revela la carta oculta y se actualiza la interfaz para reflejar los cambios en la mano y la puntuación.
        """

        decision = True
        while decision:
            self.carta_oculta = False
            self.mostrar_mano()
            puntos_crupier = self.calcular_puntuacion(self.mano_crupier)
            if puntos_crupier <= 16:
                self.pedir_carta(self.mano_crupier)
                self.interfaz.limpiar_elementos(self.curr_jugador.balance)
                self.interfaz.draw_buttons()
                self.interfaz.actualizar_puntuacion(self.calcular_puntuacion(self.mano_crupier), self.calcular_puntuacion(self.mano_jugador))
            else:
                decision = False


    def opcion_final(self):
        """
        Gestiona las opciones finales después de que termine un juego de Blackjack.

        Permite al jugador elegir entre jugar otra vez o salir del juego. La interfaz se actualiza para manejar
        los eventos finales y determinar la opción seleccionada por el jugador.

        Returns
        -------
        str
            La opción seleccionada por el jugador. Puede ser:
            - 'jugar': Si el jugador elige jugar otra vez.
            - 'salir': Si el jugador elige salir del juego.
        """

        seguir = True
        while seguir:
            opcion = self.interfaz.handle_final_events()
            if opcion == 'jugar':
                seguir = False
            elif opcion == 'salir':
                seguir = False

        return opcion


    def gestion_apuesta(self):
        """
        Gestiona el proceso de apuestas en el juego de Blackjack.

        Permite al jugador realizar apuestas incrementando la cantidad de la apuesta con valores específicos.
        La interfaz se actualiza continuamente para mostrar el saldo del jugador y la cantidad apostada.

        Returns
        -------
        int
            La cantidad total apostada por el jugador.
        """

        seguir = True
        apuesta = 0
        self.interfaz.mostrar_saldo(self.curr_jugador.balance)
        self.interfaz.draw_apuesta()
        self.interfaz.mostrar_apuesta(apuesta)
        while seguir:
            cantidad = self.interfaz.handle_apuestas()
            if cantidad == False:
                seguir = False
                self.interfaz.limpiar_elementos(self.curr_jugador.balance)
            elif cantidad in [1,5,10,25,50,100]:
                apuesta += cantidad
                self.interfaz.limpiar_elementos(self.curr_jugador.balance)
                self.interfaz.draw_apuesta()
                self.interfaz.mostrar_apuesta(apuesta)

        if apuesta > self.curr_jugador.balance or apuesta == 0:
            font = pygame.font.Font(None, 45)
            text = font.render('Cantidad inválida', True, rojo)
            text_rect = text.get_rect(center=(740, 600))
            self.pantalla.blit(text, text_rect)
            pygame.display.update()
            return False
        else:
            return apuesta




    def main_blackjack(self):
        """
        Ejecuta el bucle principal del juego de Blackjack.

        Gestiona el flujo completo de una partida de Blackjack, incluyendo la gestión de apuestas,
        la distribución de cartas, los turnos del jugador y del crupier, y la determinación del resultado final.
        También maneja la actualización de la interfaz y del saldo del jugador.
        """

        juego = True
        while juego:
            # Gestionar apuestas
            apuesta = False
            while apuesta == False:
                apuesta = self.gestion_apuesta()
            self.interfaz.draw_buttons()

            # Distribuir dos cartas al jugador y al crupier
            for i in range(2):
                self.pedir_carta(self.mano_jugador)
                self.pedir_carta(self.mano_crupier)

            # Crear una mano provisional del crupier para mostrar solo una carta
            mano_crupier_provisional = self.mano_crupier.copy()
            mano_crupier_provisional[0] = ('0')

            # Actualizar la puntuación mostrada
            self.interfaz.actualizar_puntuacion(
                self.calcular_puntuacion(mano_crupier_provisional),
                self.calcular_puntuacion(self.mano_jugador)
            )

            # Mostrar las manos en la interfaz
            self.mostrar_mano()

            # Turno del jugador
            self.turno_jugador(mano_crupier_provisional)

            # Turno del crupier si el jugador no ha perdido
            if self.calcular_puntuacion(self.mano_jugador) < 21:
                self.turno_crupier()

            # Comparar manos y determinar el resultado
            resultado = self.comparar_mano()

            # Limpiar la interfaz y actualizar la puntuación final
            self.interfaz.limpiar_elementos(self.curr_jugador.balance)
            self.interfaz.actualizar_puntuacion(
                self.calcular_puntuacion(self.mano_crupier),
                self.calcular_puntuacion(self.mano_jugador)
            )
            self.mostrar_mano()

            # Mostrar el resultado del juego
            self.interfaz.mostrar_resultado(resultado)

            # Actualizar el saldo del jugador según el resultado
            if resultado == 'BLACKJACK':
                self.curr_jugador.balance += 2 * apuesta
            elif resultado == 'Has ganado':
                self.curr_jugador.balance += apuesta
            elif resultado == 'Has perdido':
                self.curr_jugador.balance -= apuesta



            # Mostrar las opciones de jugar de nuevo o salir
            self.interfaz.draw_play()
            opcion = self.opcion_final()

            # Reiniciar el juego o salir según la opción del jugador
            if opcion == 'jugar':
                self.mano_crupier = []
                self.mano_jugador = []
                self.carta_oculta = True
                self.interfaz.limpiar_elementos(self.curr_jugador.balance)
            elif opcion == 'salir':
                juego = False
                self.terminar_juego()

    def terminar_juego(self):
        pygame.display.quit()
        self.pantalla = None
