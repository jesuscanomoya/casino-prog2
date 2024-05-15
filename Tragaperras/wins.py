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
