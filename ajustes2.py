# Ajustes de pantalla
tamaño_ventana = (300, 300)  # Define el tamaño de la ventana del juego.
fps = 120  # Define los fotogramas por segundo del juego.
altura = 1000  # Define la altura de la ventana del juego.
anchura = 1600  # Define la anchura de la ventana del juego.

# AJUSTES TRAGAPERRAS
# Imagenes
fondo = "Tragaperras/R.jpg"  # Define la ruta de la imagen de fondo del juego.
camino_simbolos = "Tragaperras/simbolos"  # Define la ruta de las imágenes de los símbolos del juego.
indices_juego = [1, 2, 3]  # Define los índices de los carretes que están en el área de juego.

# Posicion carretes
inicio_x, inicio_y = 100, -200  # Define la posición inicial de los carretes en la ventana del juego.
x_offset, y_offset = 40, 100  # Define el desplazamiento en x e y de los carretes.

color_boton = "White"  # Define el color de los botones del juego.

# Simbolos
simbolos = {
    "C++": f"{camino_simbolos}/Cereza.png",  # Define la ruta de la imagen del símbolo "C++".
    "JavaScript": f"{camino_simbolos}/sietes.png",  # Define la ruta de la imagen del símbolo "JavaScript".
    "Python": f"{camino_simbolos}/limon.png",  # Define la ruta de la imagen del símbolo "Python".
    "Sql": f"{camino_simbolos}/melocoton.png",  # Define la ruta de la imagen del símbolo "Sql".
    "Swift": f"{camino_simbolos}/platano.png"  # Define la ruta de la imagen del símbolo "Swift".
}

# texto
color_texto = "White"  # Define el color del texto del juego.
ui_fuente = "Tragaperras/Nightmare Codehack.otf"  # Define la fuente del texto del juego.
ui_tamaño_fuente = 65  # Define el tamaño de la fuente del texto del juego.
win_tamaño_fuente = 110  # Define el tamaño de la fuente del texto de victoria del juego.