
import pygame  # Importa la biblioteca Pygame, que es usada para crear videojuegos.
import random  # Importa el módulo random, que se usa para generar números aleatorios.

from ajustes2 import *  # Importa todas las variables y funciones del módulo 'ajustes'.

class Carrete:  # Define una clase llamada 'Carrete'.
    """
    Clase Carrete: Gestiona la lógica de un carrete de la máquina tragaperras.

    Atributos
    ---------
    lista_simbolo : pygame.sprite.Group
        Un grupo de sprites que contiene los símbolos del carrete.
    key_aleatoria : list
        Una lista de las claves del diccionario 'simbolos'.
    carrete_girando : bool
        Un booleano que indica si el carrete está girando o no.
    tiempo_delay : int
        El tiempo de retraso antes de que el carrete comience a girar.
    tiempo_giro : int
        El tiempo que el carrete está girando.

    Métodos
    -------
    animacion(tiempo_delta)
        Realiza la animación del giro del carrete.
    empezar_giro(tiempo_delay)
        Comienza el giro del carrete.
    giro_carrete_resultado()
        Obtiene el resultado del giro del carrete.
    """

    def __init__(self, posicion):  # Define el método inicializador de la clase.
        """
        Parámetros
        ----------
        posicion : tuple
            La posición inicial del carrete.
        """
        self.lista_simbolo = pygame.sprite.Group()  # Crea un nuevo grupo de sprites.
        self.key_aleatoria = list(
            simbolos.keys())  # Obtiene una lista de las claves del diccionario 'simbolos'.
        random.shuffle(self.key_aleatoria)  # Mezcla aleatoriamente la lista de claves.

        self.carrete_girando = False  # Inicializa una variable booleana que indica si el carrete está girando o no.

        # Sonidos
        # self.parar_sonido = pygame.mixer.Sound("Sonidos/parar.mp3")
        # self.parar_sonido.set_volume(0.9)

        for indice, item in enumerate(self.key_aleatoria):  # Recorre la lista de claves mezclada.
            self.lista_simbolo.add(Simbolo(simbolos[item], posicion,indice))  # Crea un nuevo símbolo y lo añade al grupo de sprites.
            posicion = list(posicion)  # Convierte la tupla 'posicion' en una lista.
            posicion[1] += 300  # Incrementa el segundo elemento de la lista 'posicion' en 300.
            posicion = tuple(posicion)  # Convierte la lista 'posicion' de nuevo en una tupla.

    def animacion(self, tiempo_delta):  # Define el método 'animacion' de la clase.
        """
        Parámetros
        ----------
        tiempo_delta : float
            El tiempo transcurrido desde la última actualización.
        """
        if self.carrete_girando:  # Si el carrete está girando...
            self.tiempo_delay -= (
                    tiempo_delta * 1000)  # Decrementa 'tiempo_delay' en 'tiempo_delta' multiplicado por 1000.
            self.tiempo_giro -= (
                    tiempo_delta * 1000)  # Decrementa 'tiempo_giro' en 'tiempo_delta' multiplicado por 1000.
            carrete_parando = False  # Inicializa una variable booleana que indica si el carrete está parando o no.

            if self.tiempo_giro < 0:  # Si 'tiempo_giro' es menor que 0...
                carrete_parando = True  # El carrete está parando.

            if self.tiempo_delay <= 0:  # Si 'tiempo_delay' es menor o igual que 0...

                for simbolo in self.lista_simbolo:  # Recorre todos los símbolos en el grupo de sprites.
                    simbolo.rect.bottom += 100  # Incrementa la posición inferior del rectángulo del símbolo en 100.

                    if simbolo.rect.top == 1300:  # Si la posición superior del rectángulo del símbolo es igual a 1300...
                        if carrete_parando:  # Si el carrete está parando...
                            self.carrete_girando = False  # El carrete deja de girar.
                            # self.parar_sonido.play()

                        indice_simbolo = simbolo.indice  # Obtiene el índice del símbolo.
                        simbolo.kill()  # Elimina el símbolo del grupo de sprites.

                        self.lista_simbolo.add(
                            Simbolo(simbolos[random.choice(self.key_aleatoria)], ((simbolo.valor_x), -200),
                                    indice_simbolo))  # Crea un nuevo símbolo y lo añade al grupo de sprites.

    def empezar_giro(self, tiempo_delay):  # Define el método 'empezar_giro' de la clase.
        """
        Parámetros
        ----------
        tiempo_delay : int
            El tiempo de retraso antes de que el carrete comience a girar.
        """
        self.tiempo_delay = tiempo_delay  # Establece 'tiempo_delay' al valor pasado como argumento.
        self.tiempo_giro = 1000 + tiempo_delay  # Establece 'tiempo_giro' a 1000 más el valor de 'tiempo_delay'.
        self.carrete_girando = True  # El carrete comienza a girar.

    def giro_carrete_resultado(self):
        """
        Parámetros
        ----------
        Ninguno
        """
        simbolos_giro = []
        for i in indices_juego:
            simbolos_giro.append(self.lista_simbolo.sprites()[i].tipo_simbolo)
        return simbolos_giro[::-1]

class Simbolo(pygame.sprite.Sprite):  # Define una clase llamada 'Simbolo' que hereda de 'pygame.sprite.Sprite'.
    """
    Clase Simbolo: Gestiona la lógica de un símbolo de la máquina tragaperras.

    Atributos
    ---------
    tipo_simbolo : str
        El tipo de símbolo.
    posicion : tuple
        La posición del símbolo.
    indice : int
        El índice del símbolo.
    image : pygame.Surface
        La imagen del símbolo.
    rect : pygame.Rect
        El rectángulo que encierra la imagen del símbolo.
    valor_x : int
        La posición x del lado izquierdo del rectángulo.
    tamaño_x : int
        El tamaño x del símbolo.
    tamaño_y : int
        El tamaño y del símbolo.
    alpha : int
        El valor alfa (transparencia) del símbolo.
    fade_out : bool
        Un booleano que indica si el símbolo está desvaneciéndose o no.
    fade_in : bool
        Un booleano que indica si el símbolo está apareciendo o no.

    Métodos
    -------
    update()
        Actualiza el estado del símbolo.
    """

    def __init__(self, camino_archivo, posicion, indice):  # Define el método inicializador de la clase.
        """
        Parámetros
        ----------
        camino_archivo : str
            La ruta del archivo de la imagen del símbolo.
        posicion : tuple
            La posición inicial del símbolo.
        indice : int
            El índice del símbolo.
        """
        super().__init__()  # Llama al método inicializador de la clase padre.

        self.tipo_simbolo = camino_archivo.split("/")[2].split(".")[
            0]  # Obtiene el tipo de símbolo dividiendo la ruta del archivo por '/' y '.'.

        self.posicion = posicion  # Establece la posición del símbolo.
        self.indice = indice  # Establece el índice del símbolo.
        self.image = pygame.image.load(
            camino_archivo).convert_alpha()  # Carga la imagen del símbolo y la convierte a un formato que incluye un canal alfa (transparencia).
        self.rect = self.image.get_rect(
            topleft=posicion)  # Obtiene el rectángulo que encierra la imagen del símbolo.
        self.valor_x = self.rect.left  # Obtiene la posición x del lado izquierdo del rectángulo.

        # Usado para animacion de ganar
        self.tamaño_x = 90
        self.tamaño_y = 90
        self.alpha = 200
        self.fade_out = False
        self.fade_in = False

    def update(self):  # Define el método 'update' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        if not self.fade_in and self.fade_out:
            if self.alpha > 115:
                self.alpha -= 60
                self.image.set_alpha(self.alpha)


