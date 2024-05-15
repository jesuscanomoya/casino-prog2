import pygame  # Importa la biblioteca Pygame, que es usada para crear videojuegos.
import sys  # Importa el módulo sys, que proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python.
import time  # Importa el módulo time, que proporciona funciones para trabajar con tiempos.

from jugador import Jugador  # Importa la clase 'Jugador' del módulo 'jugador'.
from carretes import *  # Importa todas las variables y funciones del módulo 'carretes'.
from ajustes import *  # Importa todas las variables y funciones del módulo 'ajustes'.
from wins import *  # Importa todas las variables y funciones del módulo 'wins'.
from ui import UI  # Importa la clase 'UI' del módulo 'ui'.

class Maquina:  # Define una clase llamada 'Maquina'.
    """
    Clase Maquina: Gestiona la lógica de la máquina tragaperras.

    Atributos
    ---------
    display_surface : pygame.Surface
        La superficie actual de la pantalla.
    balance_maquina : float
        El balance actual de la máquina.
    indice_carretes : int
        El índice actual de los carretes.
    lista_carretes : dict
        Un diccionario que almacena los carretes.
    puede_tirar : bool
        Un booleano que indica si se puede tirar o no.
    girando : bool
        Un booleano que indica si los carretes están girando o no.
    puede_animacion : bool
        Un booleano que indica si se puede realizar la animación o no.
    win_animacion_encendido : bool
        Un booleano que indica si la animación de victoria está encendida o no.
    resultado_anterior : dict
        Un diccionario que almacena el resultado anterior.
    resultado_giro : dict
        Un diccionario que almacena el resultado del giro.
    curr_jugador : Jugador
        Una instancia de la clase 'Jugador'.
    ui : UI
        Una instancia de la clase 'UI'.
    sonido_giro : pygame.mixer.Sound
        El sonido del giro.
    sonido_fila_3 : pygame.mixer.Sound
        El sonido de la fila 3.
    sonido_fila_4 : pygame.mixer.Sound
        El sonido de la fila 4.
    sonido_fila_5 : pygame.mixer.Sound
        El sonido de la fila 5.
    velocidad_cambio : float
        La velocidad de cambio.
    ultimo_cambio_tiempo : int
        El último tiempo de cambio.

    Métodos
    -------
    enfriamiento()
        Controla el enfriamiento de la máquina.
    input()
        Gestiona las entradas del usuario.
    dibujar_carrete(tiempo_delta)
        Dibuja el carrete en la pantalla.
    spawn_carretes()
        Crea los carretes.
    tirada()
        Realiza un giro de los carretes.
    obtener_resultado()
        Obtiene el resultado del giro.
    chekear_win(resultado)
        Comprueba si el resultado es una victoria.
    """
    def __init__(self):  # Define el método inicializador de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        self.display_surface = pygame.display.get_surface()  # Obtiene la superficie actual de la pantalla.
        self.balance_maquina = 10000.00
        self.indice_carretes = 0  # Inicializa el índice de los carretes a 0.
        self.lista_carretes = {}  # Inicializa un diccionario vacío para almacenar los carretes.
        self.puede_tirar = True  # Inicializa una variable booleana que indica si se puede tirar o no.
        self.girando = False  # Inicializa una variable booleana que indica si los carretes están girando o no.
        self.puede_animacion = False
        self.win_animacion_encendido = False

        # resultados
        self.resultado_anterior = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.resultado_giro = {0: None, 1: None, 2: None, 3: None, 4: None}

        self.spawn_carretes()  # Llama al método 'spawn_carretes' para crear los carretes.
        self.curr_jugador = Jugador()
        self.ui = UI(self.curr_jugador)

        # importar sonidos
        self.sonido_giro = pygame.mixer.Sound("Sonidos/giro.mp3")
        self.sonido_giro.set_volume(0.05)
        self.sonido_fila_3 = pygame.mixer.Sound("Sonidos/win_3.mp3")
        self.sonido_fila_3.set_volume(0.9)
        self.sonido_fila_4 = pygame.mixer.Sound("Sonidos/win_4.mp3")
        self.sonido_fila_4.set_volume(0.9)
        self.sonido_fila_5 = pygame.mixer.Sound("Sonidos/win_5.mp3")
        self.sonido_fila_5.set_volume(0.9)

        self.velocidad_cambio = 0.1  # Ajusta la velocidad de cambio aquí (en segundos)
        self.ultimo_cambio_tiempo = 0

    def enfriamiento(self):  # Define el método 'enfriamiento' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        for carrete in self.lista_carretes:  # Recorre todos los carretes en la lista de carretes.
            if self.lista_carretes[carrete].carrete_girando:  # Si el carrete actual está girando...
                self.puede_tirar = False  # No se puede tirar.
                self.girando = True  # Los carretes están girando.

        if not self.puede_tirar and [self.lista_carretes[carrete].carrete_girando for carrete in
                                     self.lista_carretes].count(
                False) == 5:  # Si no se puede tirar y todos los carretes han dejado de girar...
            self.puede_tirar = True  # Se puede tirar.
            self.resultado_giro = self.obtener_resultado()

            if self.chekear_win(self.resultado_giro):
                self.datos_win = self.chekear_win(self.resultado_giro)
                #Sonido de win
                self.poner_musica_win(self.datos_win)
                self.pagar_jugador(self.datos_win, self.curr_jugador)
                self.win_animacion_encendido = True
                self.ui.win_angulo_texto = random.randint(-4, 4)

    def input(self):  # Define el método 'input' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.puede_tirar and self.curr_jugador.balance >= self.curr_jugador.tamaño_apuesta:  # Si la tecla espacio está siendo presionada...
            self.tirada()  # Llama al método 'tirada'.
            self.tiempo_tirada = pygame.time.get_ticks()  # Obtiene el tiempo actual en milisegundos desde que se inicializó Pygame.
            self.curr_jugador.poner_apuesta()
            self.balance_maquina += self.curr_jugador.tamaño_apuesta
            self.curr_jugador.ultimo_pago = None

        elif keys[pygame.K_SPACE] and self.puede_tirar and self.curr_jugador.balance < self.curr_jugador.tamaño_apuesta:
            self.ui.ajustar_apuesta()
            self.tirada()  # Llama al método 'tirada'.
            self.tiempo_tirada = pygame.time.get_ticks()  # Obtiene el tiempo actual en milisegundos desde que se inicializó Pygame.
            self.curr_jugador.poner_apuesta()
            self.balance_maquina += self.curr_jugador.tamaño_apuesta
            self.curr_jugador.ultimo_pago = None

        elif keys[pygame.K_UP] and self.puede_tirar and self.curr_jugador.balance > self.curr_jugador.tamaño_apuesta:
            if time.time() - self.ultimo_cambio_tiempo > self.velocidad_cambio:
                self.ui.aumentar_apuesta()
                self.ultimo_cambio_tiempo = time.time()

        elif keys[pygame.K_DOWN] and self.puede_tirar and self.curr_jugador.balance > self.curr_jugador.tamaño_apuesta:
            if time.time() - self.ultimo_cambio_tiempo > self.velocidad_cambio:
                self.ui.diminuir_apuesta()
                self.ultimo_cambio_tiempo = time.time()
    def dibujar_carrete(self, tiempo_delta):  # Define el método 'dibujar_carrete' de la clase.
        """
        Parámetros
        ----------
        tiempo_delta : float
            El tiempo transcurrido desde la última actualización.
        """
        for carrete in self.lista_carretes:  # Recorre todos los carretes en la lista de carretes.
            self.lista_carretes[carrete].animacion(tiempo_delta)  # Llama al método 'animacion' del carrete actual.

    def spawn_carretes(self):  # Define el método 'spawn_carretes' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        if not self.lista_carretes:  # Si la lista de carretes está vacía...
            x_topleft, y_topleft = 280, -200  # Establece las coordenadas iniciales de la esquina superior izquierda de los carretes.

        while self.indice_carretes < 5:  # Mientras el índice de los carretes sea menor que 5...
            if self.indice_carretes > 0:  # Si el índice de los carretes es mayor que 0...
                x_topleft, y_topleft = x_topleft + (
                        200 + x_offset), y_topleft  # Actualiza las coordenadas de la esquina superior izquierda de los carretes.

            self.lista_carretes[self.indice_carretes] = Carrete((x_topleft,
                                                                 y_topleft))  # Crea un nuevo carrete en la posición especificada y lo añade a la lista de carretes.
            self.indice_carretes += 1  # Incrementa el índice de los carretes.

    def tirada(self):  # Define el método 'tirada' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        if self.puede_tirar:  # Si se puede tirar...
            self.tiempo_tirada = pygame.time.get_ticks()  # Obtiene el tiempo actual en milisegundos desde que se inicializó Pygame.
            self.girando = not self.girando
            self.puede_tirar = False  # Establece que no se puede tirar.

            for carrete in self.lista_carretes:  # Recorre todos los carretes en la lista de carretes.
                self.lista_carretes[carrete].empezar_giro(
                    int(carrete) * 200)  # Llama al método 'empezar_giro' del carrete actual.
                self.sonido_giro.play()
                self.win_animacion_encendido = False

    def obtener_resultado(self):
        """
        Parámetros
        ----------
        Ninguno
        """
        for carrete in self.lista_carretes:
            self.resultado_giro[carrete] = self.lista_carretes[carrete].giro_carrete_resultado()
        return self.resultado_giro

    def chekear_win(self, resultado):
        """
        Parámetros
        ----------
        resultado : dict
            Un diccionario que almacena el resultado del giro.
        """
        hits = {}
        horizontal = flip_horizontal(resultado)
        for fila in horizontal:
            simbolos_iguales = []
            for simbolo in fila:
                if fila.count(simbolo) > 2 and simbolo not in simbolos_iguales:
                    posible_win = [idx for idx, val in enumerate(fila) if simbolo == val]
                    if len(secuencia_larga(posible_win)) >= 3:
                        hits[horizontal.index(fila) + 1] = [simbolo, secuencia_larga(posible_win)]
                        simbolos_iguales.append(simbolo)
        if hits:
            self.puede_animacion = True
            return hits

    def pagar_jugador(self, datos_win, curr_jugador):  # Define el método 'pagar_jugador' de la clase.
        """
        Parámetros
        ----------
        datos_win : dict
            Un diccionario que almacena los datos de la victoria.
        curr_jugador : Jugador
            Una instancia de la clase 'Jugador'.
        """
        multiplicador = 0

        for v in datos_win.values():
            multiplicador += len(v[1])
        giro_pago = (multiplicador * curr_jugador.tamaño_apuesta)
        curr_jugador.balance += giro_pago
        self.balance_maquina -= giro_pago
        curr_jugador.ultimo_pago = giro_pago
        curr_jugador.total_ganado += giro_pago

    def poner_musica_win(self, datos_win):  # Define el método 'poner_musica_win' de la clase.
        """
        Parámetros
        ----------
        datos_win : dict
            Un diccionario que almacena los datos de la victoria.
        """
        sum = 0
        for item in datos_win.values():
            sum += len(item[1])
        if sum == 3:
            self.sonido_fila_3.play()
        elif sum == 4:
            self.sonido_fila_4.play()
        elif sum > 4:
            self.sonido_fila_5.play()

    def animacion_win(self):  # Define el método 'animacion_win' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        if self.win_animacion_encendido and self.datos_win:
            for k, v in list(self.datos_win.items()):
                if k == 1:
                    fila_animacion = 3
                elif k == 3:
                    fila_animacion = 1
                else:
                    fila_animacion = 2
                columnas_animacion = v[1]
                for carrete in self.lista_carretes:
                    if carrete in columnas_animacion and self.puede_animacion:
                        self.lista_carretes[carrete].lista_simbolo.sprites()[fila_animacion].fade_in = True
                    for simbolo in self.lista_carretes[carrete].lista_simbolo:
                        if not simbolo.fade_in:
                            simbolo.fade_out = True

    def actualizar(self, tiempo_delta):  # Define el método 'actualizar' de la clase.
        """
        Parámetros
        ----------
        tiempo_delta : float
            El tiempo transcurrido desde la última actualización.
        """
        self.enfriamiento()
        self.input()  # Llama al método 'input' para procesar la entrada del usuario.
        self.dibujar_carrete(tiempo_delta)  # Llama al método 'dibujar_carrete' para dibujar los carretes.
        for carrete in self.lista_carretes:  # Recorre todos los carretes en la lista de carretes.
            self.lista_carretes[carrete].lista_simbolo.draw(
                self.display_surface)  # Dibuja los símbolos del carrete actual en la superficie de la pantalla.
            self.lista_carretes[carrete].lista_simbolo.update()  # Actualiza los símbolos del carrete actual.
        self.ui.actualizar()
        self.animacion_win()
