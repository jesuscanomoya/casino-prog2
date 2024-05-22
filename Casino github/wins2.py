# Funciones para detectar wins

def flip_horizontal(resultado):
    """
    Función que rota una matriz 90 grados en sentido horario y luego invierte cada fila.

    Parámetros
    ----------
    resultado : dict
        Un diccionario que almacena el resultado del giro.

    Retorna
    -------
    valores_horizontal3 : list
        La matriz rotada e invertida.
    """
    # Darle la vuelta a horizontal para hacer una lista más fácil de leer
    valores_horizontal = []
    for valor in resultado.values():
        valores_horizontal.append(valor)

    # Rotar 90º para obtener la representación del giro en orden
    filas, columnas = len(valores_horizontal), len(valores_horizontal[0])
    valores_horizontal2 = [[""] * filas for _ in range(columnas)]
    for x in range(filas):
        for y in range(columnas):
            valores_horizontal2[y][filas - x - 1] = valores_horizontal[x][y]
    valores_horizontal3 = [item[::-1] for item in valores_horizontal2]
    return valores_horizontal3


def secuencia_larga(hit):
    """
    Función que encuentra la subsecuencia más larga en orden ascendente.

    Parámetros
    ----------
    hit : list
        Una lista de números.

    Retorna
    -------
    hit[inicio:final] : list
        La subsecuencia más larga en orden ascendente.
    """
    sub_seq_longitud, larga = 1, 1
    inicio, final = 0, 0
    for i in range(len(hit) - 1):
        if hit[i] == hit[i + 1] - 1:
            sub_seq_longitud += 1
            if sub_seq_longitud > larga:
                larga = sub_seq_longitud
                inicio = i + 2 - sub_seq_longitud
                final = i + 2
            else:
                sub_seq_longitud = 1
    return hit[inicio:final]
'''
Función flip_horizontal(resultado): Esta función toma un diccionario resultado como entrada, 
que representa el resultado de un giro de la máquina tragaperras. 
La función convierte este diccionario en una lista de listas (una matriz), rota esta matriz 90 grados en sentido horario y luego invierte cada fila. 
El propósito de esta función es transformar la representación del resultado del giro para que sea más fácil de leer y trabajar con ella en las siguientes etapas de la lógica del juego.
Función secuencia_larga(hit): Esta función toma una lista hit como entrada, que representa una secuencia de números. La función busca la subsecuencia más larga en esta lista que esté en orden ascendente. 
Esta función se utiliza para determinar las combinaciones ganadoras en la máquina tragaperras. 
Por ejemplo, si la lista hit es [1, 2, 3, 5, 6, 7, 9], la función devolverá [5, 6, 7], que es la subsecuencia más larga en orden ascendente.
Ahora, veamos cómo se utilizan estas funciones en el método chekear_win(resultado):

El método chekear_win(resultado) toma un diccionario resultado como entrada, que representa el resultado de un giro de la máquina tragaperras. 
Este método comprueba si el resultado del giro es una combinación ganadora.

Primero, se utiliza la función flip_horizontal(resultado) para transformar la representación del resultado del giro. 
Luego, para cada fila en el resultado transformado, se comprueba si hay algún símbolo que aparezca más de dos veces. 
Si es así, se obtiene una lista de los índices de todas las apariciones de ese símbolo en la fila. 
A continuación, se utiliza la función secuencia_larga(hit) para encontrar la subsecuencia más larga en orden ascendente en esta lista de índices. 
Si la longitud de esta subsecuencia es mayor o igual a 3, se considera una combinación ganadora.
'''